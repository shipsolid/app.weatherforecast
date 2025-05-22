# dotnet--MicroservicesBasics

## Play.Catalog

```sh
dotnet new webapi -n Play.Catalog.service
dotnet new webapi -n WeatherForecast.service --framework net8.0



dotnet tool update -g linux-dev-certs
dotnet linux-dev-certs install

dotnet dev-certs https --clean
dotnet dev-certs https --trust

dotnet build
dotnet run

https://127.0.0.1:7188/weatherforecast
http://127.0.0.1:5214/weatherforecast
```
