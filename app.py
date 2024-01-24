
from flask import Flask
from flask import render_template, request, redirect, session
from flaskext.mysql import MySQL
from datetime import datetime
from flask import send_from_directory
import os
import threading
import atexit
from multiprocessing import Process
   
##########################
##########################
#pip install selenium
#pip install webdriver_manager

import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
#
from selenium.webdriver.chrome.service import Service
#
#from werkzeug.local import _request_ctx_stack

app= Flask(__name__)
app.secret_key="barcelona"
mysql=MySQL()

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='python'
mysql.init_app(app)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/img/<imagen>')
def imagenes(imagen):
    print(imagen)
    return send_from_directory(os.path.join('templates/sitio/img'), imagen)


@app.route('/admin/cerrar')
def admin_login_cerrar():
    session.clear()
    return redirect('/admin/login')


@app.route("/css/<archivoscss>")
def css_link(archivoscss):
    return send_from_directory(os.path.join('templates/sitio/css'), archivoscss)




    
    




def ejecutar_codigo(username, password, target_url):
    try:
        ruta = os.getcwd()
        driver_path = '{}\chromedriver.exe'.format(ruta)
        opciones = webdriver.ChromeOptions()
        opciones.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opciones)
        driver.get('https://instagram.com')
        time.sleep(5)
        driver.set_window_size(500, 1000)

        # ... otras operaciones ...

        # Ingresar nombre de usuario
        username_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.click()
        username_input.send_keys(username)
        time.sleep(5)

        # Ingresar contraseña
        password_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.click()
        password_input.send_keys(password)
        time.sleep(7)

        try:
            time.sleep(2)
            login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            time.sleep(8)
        except:
            pass
        #1 Ahora no
        try:
            dementor = driver.find_element(By.XPATH,"//div[@role = 'button']").click()
            time.sleep(8)
        except:
            pass
        # Ahora no
        try:
            buttons = driver.find_elements(By.XPATH, "//*[contains(text(), 'Ahora no')]")
            for btn in buttons:
                btn.click()
            time.sleep(8)
        except:
             pass
         
        driver.get(target_url)
        
        time.sleep(10)
        driver.find_element(By.XPATH, '//a[contains(@href, "/following")]').click()
        time.sleep(10)
        
      
        scroll_box = driver.find_element(By.XPATH, "//div[@class='_aano']")
        # Definir el tiempo que deseas que dure el bucle en segundos
        tiempo_deseado = 60  # Por ejemplo, 60 segundos (1 minuto)
        # Obtener el tiempo actual en segundos
        tiempo_inicial = time.time()

        while True:
            time.sleep(2)
            ht = driver.execute_script(""" 
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight; """, scroll_box)
            time.sleep(5)
            #verificar tiempo actual nuevamente
            tiempo_actual = time.time()
            # Verificar si ha pasado el tiempo deseado
            if tiempo_actual - tiempo_inicial >= tiempo_deseado:
                break
        
        seg = driver.find_elements(By.XPATH,"//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd']")
        seg = [i.get_attribute('href') for i in seg]
        driver.maximize_window()
        
        
        
        
        while True:
                seg = driver.find_elements(By.XPATH, "//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd']")
                try:
                    seg = [i.get_attribute('href') for i in seg]
                except:
                    continue
                
                for i in seg:
                    driver.get(i)
                    time.sleep(2)
                    try:
                        seguir = driver.find_element(By.XPATH, '//div[text()="Seguir"]')
                        seguir = driver.find_element(By.XPATH, '//div[text()="Seguir"]')
                        seguir.click()
                        time.sleep(2)
                    except:
                        continue
                    
    except Exception as e:
        print('Error:', str(e))
        
    finally:
        pass
        

@app.route('/bot', methods=['GET', 'POST'])
def admin_bot():
    if request.method == 'POST':
        # Obtener datos del formulario
        username = request.form['username']
        password = request.form['password']
        target_url = request.form['target_url'] 
        # Crear un hilo para ejecutar el código, ademas con los datos del formulario
        hilo = threading.Thread(target=ejecutar_codigo, args=(username, password, target_url))
        hilo.start()

    return render_template('sitio/bot.html')



    
@app.route('/seguir', methods=['GET', 'POST'])
def follow():
    if request.method == 'POST':
        username_=request.form['username_']
        password_= request.form['password_']
        target_url_=request.form['target_url_']
        hilo= threading.Thread(target=seguir, args=(username_, password_, target_url_))
        hilo.start()
    return render_template('sitio/seguir.html')

def seguir(username_, password_, target_url_):
    try:
        ruta= os.getcwd()
        driver_path = '{}chromedriver.exe'.format(ruta)
        opciones = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=opciones)
        driver.get('https://instagram.com')
        time.sleep(5)
        driver.set_window_size(500, 1000)

        # ... otras operaciones ...

        # Ingresar nombre de usuario
        username_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.click()
        username_input.send_keys(username_)
        time.sleep(5)

        # Ingresar contraseña
        password_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.click()
        password_input.send_keys(password_)
        time.sleep(7)
        
        try:
            time.sleep(2)
            login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            time.sleep(8)
        except:
            pass
        
        #1 Ahora no
        try:
            dementor = driver.find_element(By.XPATH,"//div[@role = 'button']").click()
            time.sleep(10)
        except:
            pass
        #2 Ahora no
        try:
            buttons = driver.find_elements(By.XPATH, "//*[contains(text(), 'Ahora no')]")
            for btn in buttons:
                btn.click()
            time.sleep(8)
        except:
            pass
        
        driver.get(target_url_)
        driver.set_window_size(500, 1000)
        time.sleep(12)
        
        
        #driver.find_element(By.XPATH, "//a[contains(@href, '/following')]").click()
        #time.sleep(4)
        
        
        #scroll_box = driver.find_element(By.XPATH, "//div[@class='_aano']")
        # Definir el tiempo que deseas que dure el bucle en segundos
        #tiempo_deseado = 60  # Por ejemplo, 60 segundos (1 minuto)
        # Obtener el tiempo actual en segundos
        #tiempo_inicial = time.time()

        #while True:
        #    time.sleep(2)
        #    ht = driver.execute_script(""" 
        #    arguments[0].scrollTo(0, arguments[0].scrollHeight);
            #return arguments[0].scrollHeight; """, scroll_box)
            #time.sleep(5)
            #verificar tiempo actual nuevamente
            #tiempo_actual = time.time()
            # Verificar si ha pasado el tiempo deseado
            #if tiempo_actual - tiempo_inicial >= tiempo_deseado:
            #        break
        
        ####obteniendo lista y llendo a un href aleatorio seg[40]
        
        #seg = driver.find_elements(By.XPATH, "//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd']")

        #seg = [i.get_attribute('href') for i in seg]

        #driver.get(seg[40])
        #time.sleep(6)
        
        #driver.set_window_size(500, 1000)
        #time.sleep(15)
        
        ########################################################
        
        
        
        
        publi =driver.find_element(By.XPATH, '//ul[@class="x5ur3kl x13fuv20 x178xt8z x78zum5 x1q0g3np x1l1ennw xz9dl7a x4uap5 xsag5q8 xkhd6sd"]//li[1]//span//span').text
        time.sleep(5)
        
        
        
        
        fotos = []
        print(publi)
        ###cambiar aqui tambien el xpath, que es el mismo que fotos
        while True:
            driver.execute_script("""window.scrollTo(0,document.body.scrollHeight)""")
            time.sleep(2)
            f = driver.find_elements(By.XPATH,"//div[@class='_aabd _aa8k  _al3l']//a")
            try:
                f = [i.get_attribute('href') for i in f]
            except:
                continue
            for i in f:
                if i not in fotos:
                    fotos.append(i)
                
            print(len(fotos))
            if len(fotos) >= int(float(publi)):
                break
            
        time.sleep(8)    
        driver.maximize_window() 
        for i in fotos:
            driver.get(i)
            #click
            try:
                #click, escribir
                time.sleep(7)
                escribir = driver.find_element(By.XPATH, '//form[@class="_aidk _aidl _ak6u"]/div/textarea').click()
                time.sleep(7)
                escribir = driver.find_element(By.XPATH, '//form[@class="_aidk _aidl _ak6u"]/div/textarea').send_keys('interesante')
                time.sleep(2)
                escribir = driver.find_element(By.XPATH, '//div[@class="_akhn"]/div[2]').click()
                time.sleep(2)
                #publicar
                comment = driver.find_element(By.XPATH, '//div[@class=" _am-5"]/div').click()
                time.sleep(6)
                ########################
                escribir = driver.find_element(By.XPATH, '//div[@class="_akhn"]/div[2]').click()
                time.sleep(2)
            except:
                continue
    except Exception as e:
        print('Error:', str(e))
    finally:
        pass











@app.route('/libros')
def libros():
    
    conexion=mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `python_libros`")
    libros=cursor.fetchall()
    conexion.commit()
    
    return render_template('sitio/libros.html', libros=libros)

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/admin/')
def admin():
    
    if not 'login' in session:
        return redirect("admin/login")
    
    return render_template('admin/index.html')


@app.route('/admin/login')
def login():
    return render_template('admin/login.html')


@app.route('/admin/login', methods=['POST'])
def admin_login_post():
    _usuario=request.form['txtUsuario']
    _password=request.form['txtPassword']
    print(_usuario)
    print(_password)
    
    if _usuario=='barcelona' and _password =='999':
        session['login']=True
        session["usuario"]="Administrador"
        return render_template('admin/index.html')
    
    return render_template('admin/login.html', mensaje="Acceso denegado")


    
@app.route('/admin/libros')
def admin_libros():
    
    if not 'login' in session:
        return redirect("admin/login")
    
    conexion=mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `python_libros`")
    libros=cursor.fetchall()
    conexion.commit()
    
    
    return render_template('admin/libros.html', libros=libros)




@app.route('/admin/libros/guardar', methods=["POST"])
def admin_libros_guardar():
    
    if not 'login' in session:
        return redirect("admin/login")
    
    _nombre=request.form['txtNombre']
    _url=request.form['txtUrl']
    _archivo=request.files['txtImagen']
    
    tiempo = datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')
    
    if _archivo.filename!='':
        nuevoNombre = horaActual+'_'+_archivo.filename
        _archivo.save("templates/sitio/img/"+ nuevoNombre)
    
    sql="INSERT INTO `python_libros`(`id`, `nombre`, `imagen`, `url`) VALUES (NULL,%s,%s,%s);"
    datos=(_nombre,nuevoNombre,_url)
    conexion= mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()
    
    print(_nombre)
    print(_archivo)
    print(_archivo)
    return redirect('/admin/libros')
    
@app.route('/admin/libros/borrar',methods=['POST'])
def admin_libros_borrar():
    
    
    if not 'login' in session:
        return redirect("admin/login")
    
    
    _id=request.form['txtID']
    print(_id)
    
    
    conexion=mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT imagen FROM `python_libros` WHERE id=%s",(_id))
    libros=cursor.fetchall()
    conexion.commit()
    
    if os.path.exists("templates/sitio/img/" + str(libros[0][0])):
        os.unlink("templates/sitio/img/" + str(libros[0][0]))
    
    conexion=mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM `python_libros` WHERE id=%s",(_id))
    conexion.commit()
    
    return redirect('/admin/libros')


if  __name__ == '__main__':
   app.run(debug=True)

