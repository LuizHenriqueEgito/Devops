# Comandos Terraforms
- *funções:* manipulam dados (`merge`, `concat`, etc)
- *meta-arguments:* controlam recursos (`for_each`)

## `for_each`
```hcl
# for_each: cria múltiplos recursos dinamicamente
variable "users" {
    default = ["alice", "bob", "charlie"]
}

resource "aws_iam_user" "users" {
    for_each = toset(var.users)
    name = each.key
}
```

## `count`
```hcl
# count: mais simples que for_each (menos flexível)
resource "aws_instance" "server" {
    count = 2
    ami = "ami-123"
    instance_type = "t2.micro"
    tags = {
        Name = "server-${count.index}"
    }
}
```

## `lookup`
```hcl
# lookup: busca valor em um map com fallback, é como um get se não existir devolvemos um valor default.
variable "instance_types" {
  default = {
    dev  = "t2.micro"
    prod = "t3.large"
  }
}

locals {
  instance_type = lookup(var.instance_types, "dev", "t2.nano")
}
```

## `merge`
``` hcl
# merge: junta mútiplos maps
locals {
  default_tags = {
    Owner = "Luiz"
  }

  extra_tags = {
    Env = "dev"
  }

  tags = merge(local.default_tags, local.extra_tags)
}
```

## `concat`
```hcl
# concat: junta listas
locals {
  list1 = ["a", "b"]
  list2 = ["c", "d"]

  result = concat(local.list1, local.list2)
}
```

## `coalesce`
``` hcl
# coalesce: retorna o primeiro valor não nulo
locals {
  name = coalesce(null, "", "default-name")
}
```

## `element`
``` hcl
# element: pega elemento por indice
locals {
  zones = ["us-east-1a", "us-east-1b"]

  zone = element(local.zones, 1)
}
```

## `file`
``` hcl
# file: lê o conteúdo de um arquivo
locals {
  script = file("${path.module}/script.sh")
}
```

## `join`
```hcl
# join: junta lista em string
locals {
  names = ["alice", "bob"]

  result = join(", ", local.names)
}
```

## `split`
```hcl
# string: divide string em lista
locals {
  data = "a,b,c"

  result = split(",", local.data)
}
```

## `lenght`
```hcl
# lenght: devolve o tamanho de uma lista/map/string
locals {
  size = length(["a", "b", "c"])
}
```

## `lower` / `upper`
```hcl
locals {
  lower = lower("HELLO")  # fica minusculo
  upper = upper("hello")  # fica maiusculo
}
```

## `replace`
```hcl
# replace: substitui texto
locals {
  result = replace("hello world", "world", "terraform")
}
```

## `toset`
```hcl
# toset: remove duplicadas (e vira um set)
locals {
  result = toset(["a", "a", "b"])
}
```

## `tolist`
```hcl
# tolist: faz virar uma lista
locals {
  result = tolist(toset(["a", "b"]))
}
```

## `tomap`
```hcl
# tomap: é como um dicionario/hashmap
locals {
  result = tomap({
    a = 1
    b = 2
  })
}
```

## `jsonencode`
```hcl
# jsonencode: converte para json
locals {
  json = jsonencode({
    name = "luiz"
    age  = 30
  })
}
```

## `jsondecode`
```hcl
# jsondecode: transforma uma string em um map
```