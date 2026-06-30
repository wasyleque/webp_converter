import os
import argparse
from PIL import Image

def format_bytes(byte_count):
    """Formats bytes into a human-readable string (KB, MB, GB)."""
    if byte_count is None:
        return "0 B"
    power = 1024
    n = 0
    power_labels = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while byte_count >= power and n < len(power_labels) -1 :
        byte_count /= power
        n += 1
    return f"{byte_count:.2f} {power_labels[n]}"

def convert_images_and_update_logs(root_dir, autoremove=False, recursive=False):
    print(f"Starting process in directory: {root_dir}")
    if autoremove:
        print("AUTO-REMOVE is ENABLED. Original files will be deleted after conversion.")
    if recursive:
        print("RECURSIVE mode is ENABLED. Processing all subdirectories.")

    total_bytes_saved = 0

    # If recursive is enabled, walk through all directories
    if recursive:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            process_directory(dirpath, filenames, autoremove, total_bytes_saved)
    else:
        # Original behavior - only process subdirectories of root_dir
        for dir_name in os.listdir(root_dir):
            current_dir = os.path.join(root_dir, dir_name)

            if not os.path.isdir(current_dir):
                continue

            print(f"\nProcessing subdirectory: {current_dir}")
            
            # --- Image Conversion ---
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

                        # If autoremove is enabled, delete the original file
                        if autoremove:
                            file_size = os.path.getsize(input_path)
                            total_bytes_saved += file_size
                            os.remove(input_path)
                            print(f"  - Removed original file: {filename}")

                    except Exception as e:
                        print(f"  - Error converting {filename}: {e}")

            # --- Log File Update ---
            log_file_path = os.path.join(current_dir, 'log.html')
            if os.path.exists(log_file_path):
                try:
                    with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as f:
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

    # --- Final Summary ---
    if autoremove and total_bytes_saved > 0:
        print("\n-------------------------------------------")
        print(f"Process finished. You have just reclaimed {format_bytes(total_bytes_saved)} of space!")
        print("-------------------------------------------")
    else:
        print("\nProcess finished.")


def process_directory(current_dir, filenames, autoremove, total_bytes_saved):
    """Helper function to process a single directory."""
    print(f"\nProcessing directory: {current_dir}")
    
    # --- Image Conversion ---
    for filename in filenames:
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

                # If autoremove is enabled, delete the original file
                if autoremove:
                    file_size = os.path.getsize(input_path)
                    total_bytes_saved += file_size
                    os.remove(input_path)
                    print(f"  - Removed original file: {filename}")

            except Exception as e:
                print(f"  - Error converting {filename}: {e}")

    # --- Log File Update ---
    log_file_path = os.path.join(current_dir, 'log.html')
    if os.path.exists(log_file_path):
        try:
            with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as f:
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
    parser = argparse.ArgumentParser(
        description="Convert JPEG/PNG images to WebP and update log files within subdirectories.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--autoremove',
        action='store_true',
        help="Delete original image files after successful conversion."
    )
    parser.add_argument(
        '--dir',
        type=str,
        help="Specify the target directory for conversion (default: current directory)."
    )
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        help="Process subdirectories recursively."
    )
    args = parser.parse_args()

    target_directory = args.dir if args.dir else os.getcwd()
    convert_images_and_update_logs(target_directory, args.autoremove, args.recursive)
