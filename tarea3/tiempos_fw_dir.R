tiempos <- read.csv("tiempos_fw_dir.csv", header=F)
tiempos = t(tiempos)

t = seq(10,100,10)
datos <- matrix(tiempos,nrow=10,byrow=F)
#print(datos)

png("tiempos_fw_dir.png")
colnames(datos) = t
boxplot(datos, xlab="Nodos", ylab="Tiempos",)
graphics.off()
