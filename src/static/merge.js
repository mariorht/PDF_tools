document.addEventListener('DOMContentLoaded', () => {
    const pdfForm = document.getElementById('pdfForm');
    const preview = document.getElementById('preview');

    pdfForm.addEventListener('change', async (event) => {
        const files = event.target.files;
        for (const file of files) {
            const reader = new FileReader();
            reader.onload = async (e) => {
                const arrayBuffer = e.target.result;
                const pdf = await pdfjsLib.getDocument(arrayBuffer).promise;
                const page = await pdf.getPage(1); // Obtiene la primera página

                const viewport = page.getViewport({ scale: 0.2 }); // Ajusta la escala según sea necesario
                const canvas = document.createElement('canvas');
                const context = canvas.getContext('2d');
                canvas.width = viewport.width;
                canvas.height = viewport.height;

                const renderContext = {
                    canvasContext: context,
                    viewport: viewport
                };
                await page.render(renderContext).promise;

                const listItem = document.createElement('div');
                listItem.classList.add('preview-item');

                const fileName = document.createElement('div');
                fileName.classList.add('file-name');
                fileName.textContent = file.name;

                listItem.appendChild(canvas);
                listItem.appendChild(fileName);
                preview.appendChild(listItem);
            };
            reader.readAsArrayBuffer(file);
        }
    });
});
