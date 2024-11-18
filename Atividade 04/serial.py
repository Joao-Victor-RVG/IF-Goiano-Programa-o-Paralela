from PIL import Image
import os
import random
import time  # Importa o módulo para medir o tempo

# Função para criar imagens aleatórias
def generate_images(dataset_folder, num_images, size=(500, 500)):
    os.makedirs(dataset_folder, exist_ok=True)  # Cria o diretório, se não existir
    for i in range(1, num_images + 1):
        img = Image.new(
            "RGB",
            size,
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        )
        img.save(os.path.join(dataset_folder, f"image_{i:04d}.jpg"))

# Função para converter imagem para escala de cinza
def convert_to_grayscale_serial(image_path, output_path):
    # Abrir a imagem
    img = Image.open(image_path).convert("RGB")
    width, height = img.size
    grayscale_img = Image.new("L", (width, height))  # Criar uma imagem em escala de cinza

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            # Aplicar a fórmula
            gray = int(r * 0.298 + g * 0.587 + b * 0.114)
            grayscale_img.putpixel((x, y), gray)

    # Salvar a imagem convertida
    grayscale_img.save(output_path)

# Função para processar o dataset sequencialmente
def process_dataset_serial(dataset_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)  # Cria o diretório, se não existir

    for filename in os.listdir(dataset_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_path = os.path.join(dataset_folder, filename)
            output_path = os.path.join(output_folder, "grayscale_" + filename)
            convert_to_grayscale_serial(input_path, output_path)

# Configuração inicial
if __name__ == "__main__":
    # Definir pastas
    dataset_folder = "datasets/images"
    output_folder = "output_images"

    # Número de imagens
    num_images = 1000  # Altere para 1, 10, 100 ou 1000

    # Temporizador para geração de imagens
    print(f"Gerando {num_images} imagens no diretório {dataset_folder}...")
    start_time = time.time()  # Início do cronômetro
    generate_images(dataset_folder, num_images)
    end_time = time.time()  # Fim do cronômetro
    generation_time = end_time - start_time
    print(f"Imagens geradas em {generation_time:.2f} segundos.")

    # Temporizador para processamento serial
    print(f"Convertendo imagens para escala de cinza no diretório {output_folder}...")
    start_time = time.time()  # Início do cronômetro
    process_dataset_serial(dataset_folder, output_folder)
    end_time = time.time()  # Fim do cronômetro
    processing_time = end_time - start_time
    print(f"Imagens convertidas em {processing_time:.2f} segundos.")

    # Resumo final
    print("\nResumo do processo:")
    print(f"- Tempo para gerar imagens: {generation_time:.2f} segundos.")
    print(f"- Tempo para processar imagens: {processing_time:.2f} segundos.")
