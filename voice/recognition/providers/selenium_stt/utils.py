def stream_text(content: str) -> None:
    print("\033[96m\rUser Speaking: \033[93m" + f" {content}", end='', flush=True)
