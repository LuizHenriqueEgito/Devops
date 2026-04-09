import time
import random
from enum import Enum
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

class UserChoice(Enum):
    ONE = '1'
    TWO = '2'
    THREE = '3' 

def menu() -> None:
    console.clear()
    painel = Panel(
        "[bold cyan]Terminal Customizado[/bold cyan]\n\n"
        "[1] Jogar moeda\n"
        "[2] Jogar dado\n"
        "[3] Sair",
        title="Menu",
        border_style="green"
    )
    console.print(painel)
    return None

def coin():
    result = random.choice(['K', 'C'])
    console.print(f"\n[bold yellow]Resultado:[/bold yellow] {result}")
    time.sleep(2)

def dice():
    result = random.randint(1, 6)
    console.print(f"\n[bold magenta]Resultado:[/bold magenta] {result}")
    time.sleep(2)

def main():
    while True:
        menu()
        user = Prompt.ask('\nEscolha uma opção', choices=['1', '2', '3'])

        match UserChoice(user):
            case UserChoice.ONE:
                coin()
            case UserChoice.TWO:
                dice()
            case UserChoice.THREE:
                console.print('\n[bold red]Encerrando...[/bold red]')
                break

if __name__ == '__main__':
    main()