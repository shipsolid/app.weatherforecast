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

http://localhost:5101/weatherforecast

https://127.0.0.1:7188/weatherforecast
http://127.0.0.1:5214/weatherforecast
```

```sh
pip install -r requirements.txt

REPO="digital/dev" \
GITHUB_TOKEN="ghp_123abc..." \
ISSUE_NUMBER="42" \
python3 thanks.py


```
