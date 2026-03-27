nodo1.run("backup.sh")

grupoA.update()

deploy app1 to grupoA

nodo1.temp > 30 -> nodo1.run("cooling.sh")

parallel {
    nodo2.run("backup.sh")
    nodo3.run("backup.sh")
}