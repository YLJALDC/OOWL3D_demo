import os
from glob import glob

def create_root_html(classes):
    model_num = 0
    for c in classes:
        model_num += len(os.listdir("./models/" + c))
        
    with open('./index.html', 'w') as f:
        f.write("<!doctype html>\n\
<html lang=\"en\">\n\
<head>\n\
<meta charset=\"utf-8\">\n\
<meta http-equiv=\"x-ua-compatible\" content=\"ie=edge\">\n\
<title>OOWL3d</title>\n\
<link rel=\"stylesheet\" href=\"static/css/normalize.css\">\n\
<link rel=\"stylesheet\" href=\"static/themes/classic/galleria.classic.css\">\n\
<link rel=\"stylesheet\" href=\"static/css/style.css\">\n\
</head>\n\
<body>\n\
<div class=\"container\">\n\
<header>\n\
<h1><a href=\"./index.html\">OOWL3d</a></h1>\n\
<p> This is a visual demo website for OOWL3D dataset provided by UC San Diego Statistical Visual Computing Lab. This dataset is still expanding and currently contains "+ str(model_num)+ " models. It takes some time to load the model. This is only for visualization purpose, please open the original file with Meshlab for further details. If you would like to contribute a new segemented model, please refer to readme.</p>\n\
</header>\n\
<div id=\"main\" role=\"main\">\n\
<div id=\"albums\">\n\
<ul>"
)
        for c in classes:
            f.write("<li><a href=\"./models/"+ c + "/index2.html\">\
<span class=\"album_title\">" + c +"</span></a></li>")
        
        f.write("</ul>\n</div>\n </div>\n </div>\n </body>\n </html>")
        
def create_class_html(cls, objs):
    model_num = len(os.listdir("./models/" + cls))
    with open('./models/' + cls + '/index2.html', 'w') as f:
        f.write("<!doctype html>\n\
<html lang=\"en\">\n\
<head>\n\
<meta charset=\"utf-8\">\n\
<meta http-equiv=\"x-ua-compatible\" content=\"ie=edge\">\n\
<title>OOWL3d</title>\n\
<link rel=\"stylesheet\" href=\"../../static/css/normalize.css\">\n\
<link rel=\"stylesheet\" href=\"../../static/themes/classic/galleria.classic.css\">\n\
<link rel=\"stylesheet\" href=\"../../static/css/style.css\">\n\
</head>\n\
<body>\n\
<div class=\"container\">\n\
<header>\n\
<h1><a href=\"../../index.html\">Home</a></h1>\n\
<h1><a href=\"./index2.html\">" + str(model_num) + ' ' + cls + "</a></h1>\n\
</header>\n\
<div id=\"main\" role=\"main\">\n\
<div id=\"albums\">\n\
<ul>"
)
        for obj in objs:
            f.write("<li><a href=\"./"+ obj + "/index2.html\">\
<span class=\"album_title\">" + obj +"</span></a></li><br>")
        
        f.write("</ul>\n</div>\n </div>\n </div>\n </body>\n </html>")
        
def create_model_html(cls, obj):
   
    # read .obj
    obj_file = [n for n in os.listdir('./models/' + cls + '/' + obj) if n[-3:] == 'obj']
    if len(obj_file) == 0:
        obj_file = ""
    else:
        obj_file = obj_file[0]
    
	# read meta data
    model_meta = "self-scanning"
    if os.path.exists('./models/' + cls + '/' + obj +'/meta.txt'):
	    with open('./models/' + cls + '/' + obj +'/meta.txt', 'r') as f:
                lines = f.readlines()
            model_meta = lines[0]
    with open('./models/' + cls + '/' + obj +'/index2.html', 'w') as f:
        f.write("\
<!DOCTYPE HTML>\n\
<HTML>\n\
<HEAD>\n\
<TITLE> " + obj +\
"</TITLE>\n\
</HEAD>\n\
<BODY>\n\
<h1><a href=\"../../../index.html\">Home</a> <a href=\"../index2.html\">" + cls + "</a></h1>\n\
<p>This model is collected by " + model_meta + "</p>\
<div style=\"width:960px; margin:auto; position:relative; font-size: 9pt; color: \#FFFFFF;\"\>\n\
<canvas id=\"cv\"  width=\"960\" height=\"960\" ></canvas>\n\
</div>\n\
<script type=\"text/javascript\" src=\"../../../jsc3d.js\"></script>\n\
<script type=\"text/javascript\" src=\"../../../jsc3d.touch.js\"></script>\n\
<script type=\"text/javascript\" src=\"../../../jsc3d.webgl.js\"></script>\n\
<script type=\"text/javascript\">\n\
var canvas = document.getElementById(\'cv\');\n\
var viewer = new JSC3D.Viewer( canvas, {SceneUrl:\'" + obj_file +\
"\',InitRotationX: 30,\
BackgroundColor1: \'\#FFFFFF\',\
BackgroundColor2: \'\#FFFFFF\',\
RenderMode: \'texture\',\
Renderer: \'webgl\'\
});\n\
viewer.init();\n\
viewer.update();\n\
viewer.onmousemove = function(x, y, button, depth, mesh) {\
canvas.style.cursor = mesh ? \'pointer\' : \'\';\
};\n\
</script>\n\
</BODY>\n\
</HTML>"
)
        
        
if __name__ == '__main__':
    data_root = './models'
    classes = sorted(os.listdir(data_root))
    create_root_html(classes)
    for c in classes:
        objs = [i.split('/')[-2] for i in glob(os.path.join(data_root,c) + '/*/')]
        #print(objs)
        create_class_html(c, objs)
        for obj in objs:
            create_model_html(c, obj)
