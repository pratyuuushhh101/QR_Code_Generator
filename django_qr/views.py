from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import base64
from io import BytesIO

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # Generate QR in memory
            qr = qrcode.make(url)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")

            qr_base64 = base64.b64encode(buffer.getvalue()).decode()

            context = {
                'res_name': res_name,
                'qr_base64': qr_base64,
                'file_name': f"{res_name.replace(' ', '').lower()}_menu.png"
            }

            return render(request, 'qr_result.html', context)
    else:
        form = QRCodeForm()

    return render(request, 'generate_qr_code.html', {'form': form})
