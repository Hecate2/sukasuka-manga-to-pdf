from PIL import Image
from natsort import natsorted
import os


def images2pdf(folderPath, pdfFilePath):
    files = natsorted(os.listdir(folderPath))
    pngFiles = []
    sources = []
    for file in files:
        if file.endswith('.png') or file.endswith('.jpg'):
            pngFiles.append(os.path.join(folderPath, file))
    pngFiles.sort()
    output = Image.open(pngFiles[0])
    pngFiles.pop(0)
    for file in pngFiles:
        pngFile = Image.open(file)
        if pngFile.mode == "RGB":
            pngFile = pngFile.convert("RGB")
        sources.append(pngFile)
    output.save(pdfFilePath, "pdf", save_all=True, append_images=sources)


if __name__ == "__main__":
    root_folder = "C:/末日时在做什么？漫画汉化版"
    folders = os.listdir(root_folder)
    for folder in folders:
        full_folder_path = os.path.join(root_folder, folder)
        if os.path.isdir(full_folder_path):
            images2pdf(full_folder_path, f'末日时在做什么？漫画汉化版{folder}.pdf')
