import os

tpl_dir = os.environ.get("PROMPT_TPL_DIR", "prompts")
api_spec = os.environ.get("API_SPEC", "ollama")

openai_base_url = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
openai_api_key = os.environ.get("OPENAI_API_KEY", "EMPTY")
openai_model = os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo")

google_model = os.environ.get("GOOGLE_MODEL", "models/gemini-1.5-pro")

ollama_base_url = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434/v1")
ollama_api_key = os.environ.get("OLLAMA_API_KEY", "EMPTY")
ollama_model = os.environ.get("OLLAMA_MODEL", "deepseek-coder:6.7b")


def get_config() -> dict:
    return {
        "tpl_dir": tpl_dir,
        "api_spec": api_spec,
    }


def update_config(conf: dict):
    global api_spec, tpl_dir
    api_spec = conf.get("api_spec", api_spec)
    tpl_dir = conf.get("tpl_dir", tpl_dir)


def get_api_config(api_spec: str) -> dict:
    if api_spec == "openai":
        return {
            "base_url": openai_base_url,
            "api_key": openai_api_key,
            "model": openai_model,
        }
    elif api_spec == "google":
        return {
            "base_url": None,
            "api_key": os.environ.get("GOOGLE_API_KEY"),
            "model": google_model,
        }
    elif api_spec == "ollama":
        return {
            "base_url": ollama_base_url,
            "api_key": ollama_api_key,
            "model": ollama_model,
        }
    else:
        import extension as ext

        return ext.get_api_config(api_spec)


def update_api_config(api_spec: str, conf: dict):
    global openai_base_url, openai_api_key, openai_model
    global google_model
    global ollama_base_url, ollama_api_key, ollama_model
    if api_spec == "openai":
        openai_base_url = conf.get("base_url")
        openai_api_key = conf.get("api_key")
        openai_model = conf.get("model")
    elif api_spec == "google":
        os.environ["GOOGLE_API_KEY"] = conf.get("api_key")
        google_model = conf.get("model")
    elif api_spec == "ollama":
        ollama_base_url = conf.get("base_url")
        ollama_api_key = conf.get("api_key")
        ollama_model = conf.get("model")
    else:
        import extension as ext

        ext.update_api_config(api_spec, conf)


def get_api_key():
    return get_api_config(api_spec).get("api_key")


def get_base_url():
    return get_api_config(api_spec).get("base_url")


def get_model():
    return get_api_config(api_spec).get("model")


if __name__ == "__main__":
    print(get_config())
    print(get_api_config(api_spec))
