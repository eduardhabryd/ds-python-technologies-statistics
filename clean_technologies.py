def split_technologies(x: str) -> list | str:
    x = x.lower()
    if "python3" in x:
        x = x.replace("python3", "python")
        x = x.replace("python", "")
        x = x + "/python"

    if "," in x:
        x = x.replace(",", "/")

    if "+" in x:
        x = x.replace("+", "/")

    if "/" in x:
        x = x.split('/')

    return x


def transform_technologies(x: str) -> str:
    x = x.strip()

    if len(x) == 2 and ("cd" in x or "ci" in x):
        return "ci/cd"

    if x.startswith("react"):
        return "react"

    if x.startswith("rest"):
        return "rest"

    if x.startswith("selenium"):
        return "selenium"

    if x == "ts":
        return "typescript"

    if x.startswith("unit"):
        return "unitest"

    if x.startswith("vue"):
        return "vue"

    if x.startswith("web scrap"):
        return "web scraping"

    if "kubernet" in x:
        return "kubernetes"

    if x.startswith("posgres") or x.startswith("postgres"):
        return "postgres"

    if x == "next.js":
        return "nextjs"

    if x.startswith("mongo"):
        return "mongodb"

    if x == "machine learning":
        return "ml"

    if x == "js":
        return "javascript"

    if x.startswith("full stack") or x.startswith("full-stack"):
        return "fullstack"

    if x == "django rest" or x == "drf" or x == "django-rest-framework" or x == "django rest framework":
        return "drf"

    if x == "docker compose":
        return "docker"

    if x == "fast api":
        return "fastapi"

    if x.startswith("aws"):
        return "aws"

    if x.startswith("backend"):
        return "backend"

    if x.startswith("qa"):
        return "qa"

    if x.startswith("angular"):
        return "angular"

    if x.startswith("blockchain") or x.startswith("crypto"):
        return "blockchain/crypto"

    if x.strip().startswith("docker"):
        return "docker"

    if x.startswith("data "):
        return "data science"

    if x == "postgre sql":
        return "postgres"

    return x
