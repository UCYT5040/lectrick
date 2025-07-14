def watch(file_path):
    content = None
    while True:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                new_content = f.read()
            if new_content != content:
                content = new_content
                print(f"File '{file_path}' changed:")
                print(content)
        except FileNotFoundError:
            print(f"File '{file_path}' not found. Waiting for it to be created...")
        except Exception as e:
            print(f"An error occurred: {e}")
