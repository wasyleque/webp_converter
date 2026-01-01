import os
from PIL import Image

def convert_images_and_update_logs(root_dir):
    print(f"Starting process in directory: {root_dir}")

    for dir_name in os.listdir(root_dir):
        current_dir = os.path.join(root_dir, dir_name)

        if not os.path.isdir(current_dir):
            continue

        print(f"\nProcessing subdirectory: {current_dir}")
        has_converted_files = False

        # Step 1 & 2: Find and convert all jpeg and png files
        for filename in os.listdir(current_dir):
            if filename.lower().endswith(('.png', '.jpeg', '.jpg')):
                input_path = os.path.join(current_dir, filename)
                output_filename = os.path.splitext(filename)[0] + '.webp'
                output_path = os.path.join(current_dir, output_filename)

                if os.path.exists(output_path):
                    print(f"  - Skipping {filename}, .webp version already exists.")
                    continue

                try:
                    with Image.open(input_path) as img:
                        img.save(output_path, 'webp')
                        print(f"  - Converted {filename} to {output_filename}")
                        has_converted_files = True
                except Exception as e:
                    print(f"  - Error converting {filename}: {e}")

        # Step 3 & 4: If conversions happened, edit log.html
        log_file_path = os.path.join(current_dir, 'log.html')
        if os.path.exists(log_file_path):
            try:
                with open(log_file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                new_content = content.replace('.jpeg', '.webp').replace('.png', '.webp')

                if new_content != content:
                    with open(log_file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"  - Updated log.html in {current_dir}")
                else:
                    print(f"  - log.html in {current_dir} did not need updates.")
            except Exception as e:
                print(f"  - Error processing {log_file_path}: {e}")
        else:
            print(f"  - No log.html found in {current_dir}.")


if __name__ == "__main__":
    # Get the directory where the script is located, which is the target directory
    target_directory = os.getcwd()
    convert_images_and_update_logs(target_directory)
    print("\nProcess finished.")
