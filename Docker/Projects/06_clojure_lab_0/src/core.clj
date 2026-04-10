(ns core
  (:gen-class))

(defn transformar [numeros]
  (->> numeros
    (filter even?)
    (map #(* % 2))
    (map #(+ % 10))))

(defn -main []
  (println "Digite uma lista de numeros separados por espaco:")
  (flush)
  (let [input (read-line)
        numeros (map #(Integer/parseInt %) (clojure.string/split input #" "))
        resultado (transformar numeros)]
    (println "Resultado:")
    (println resultado)))