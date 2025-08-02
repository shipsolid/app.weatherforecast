[![upper-build](https://github.com/shipsolid/app.weatherforecast/actions/workflows/upper-build.yml/badge.svg?branch=main)](https://github.com/shipsolid/app.weatherforecast/actions/workflows/upper-build.yml)
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

## Create and push tag

To **manually create and push a Git tag** from your local machine, follow these steps:

### 📍1. Open your terminal and navigate to the repo

```bash
cd path/to/your/repo
```

### 🧾2. Check existing tags

This helps avoid duplicate version numbers:

```bash
git tag
```

### 🆕3. Create a new tag

Use [semantic versioning](https://semver.org/) format like `v1.0.0`:

```bash
git tag v1.0.0
```

🔁 Alternatively, annotate it with a message:

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
```

### 🚀4. Push the tag to GitHub

```bash
git push origin v1.0.0
```

✅ This will:

* Push the tag to your remote repo
* Trigger any workflows that listen for `push` events on tags (e.g., your release workflow)

---

### 🔄 Bonus: Overwrite a tag (force update)

If you accidentally tagged the wrong commit:

```bash
# Move tag to current HEAD (or any commit SHA)
git tag -f v1.0.0

# Force push the updated tag
git push origin v1.0.0 --force
```

🛑 Be cautious when force-pushing tags, especially if others rely on them.

---

### 📦 After Pushing

You can confirm:

* The tag appears under the **"Tags"** section in your GitHub repo: `https://github.com/<owner>/<repo>/tags`
* If your workflow has a condition like `if: startsWith(github.ref, 'refs/tags/')`, it will now trigger

---
