import os
import csv


def list_files_in_folder(folder_path):
    files_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list

def write_file_paths_to_csv(file_paths, output_csv):
    with open(output_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['img_path'])
        for file_path in file_paths:
            csv_writer.writerow([file_path])

if __name__ == "__main__":
    folder_path = '/Users/makenarobison/Desktop/Computer Vision Research/converted_images/test1105' 
    output_csv = 'test1110_imgs.csv' 

    files_list = list_files_in_folder(folder_path)


    write_file_paths_to_csv(files_list, output_csv)

    print(f"CSV file '{output_csv}' created successfully with file paths.")