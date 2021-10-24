df1 <- read.table("data/simple_data.txt", header = FALSE)

df2 <- read.csv("data/simple_data.csv", header = FALSE, sep=",")

cat(df2[2,3], file = "df1_value.txt")


df_covid <- read.csv("data/covid_data.csv", header = TRUE, sep = ",")

head(df_covid)
tail(df_covid)
cat(df_covid[61895,5], file = "covid.txt")


require(XML)
data <- xmlParse("data/covid_data.xml")
df_xml <- xmlToDataFrame(data)


ta <- read.table("data/temp_anomaly.txt", skip=9, col.names = c("month", "temp_anomaly"))