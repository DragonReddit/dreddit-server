from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

@app.errorhandler(500)
@app.route('/cdn/errors/500')
async def internal_server_error(error):
	print(f'[CDN ERROR 500] {error}')
	return render_template("/errors/cdn/error_500.html"), 500

@app.errorhandler(404)
@app.route('/cdn/errors/404')
async def not_found(error):
	print(f'[CDN ERROR 404] File not found')
	return render_template("/errors/cdn/error_404.html"), 404

@app.route('/ping')
async def ping():
    return 'Pong!', 200

@app.route('/cdn/media/<path:filename>')
def cdn_media(filename):
    return send_from_directory(
        os.path.abspath('.\\cdn\\media'),
        filename,
        as_attachment=False,
        mimetype=None
    )

@app.route('/cdn/attachment/<path:filename>')
def cdn_attachment(filename):
    return send_from_directory(
        os.path.abspath('.\\cdn\\attachment'),
        filename,
        as_attachment=True
    )

app.run(debug = True, port = 7002)