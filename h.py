def ejecutar_codigo():
    
    try:
        ruta = os.getcwd()
        driver_path = '{}\chromedriver.exe'.format(ruta)
        opciones = webdriver.ChromeOptions()
        opciones.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opciones)
        driver.get('https://instagram.com')
        time.sleep(5)

        # Aquí puedes realizar cualquier otra operación que necesites en la página
        # Por ejemplo, imprimir el título de la página
        print(driver.title)
        driver.set_window_size(500, 1000)
        username= driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.click()
        username.send_keys('luislopez_1024')
        time.sleep(5)
        ###constraseña###
        username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        username.click()
        username.send_keys('barcelona')
        time.sleep(7)
        ###enviar###
        try:
            time.sleep(2)
            login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            time.sleep(5)
        except:
            pass
        
        try:
            dementor = driver.find_element(By.XPATH,"//div[@role = 'button']").click()
        except:
            pass
        # Mantener la ventana abierta, por ejemplo, pausando el hilo
        while True:
            time.sleep(10)

    except Exception as e:
        # Manejar la excepción
        print('Error:', str(e))

    finally:
        # Asegúrate de cerrar el navegador al finalizar (esto puede no ejecutarse si el hilo se pausa)
        pass

@app.route('/bot')

def admin_bot():
    
    
    # Crear un hilo para ejecutar el código
    hilo = threading.Thread(target=ejecutar_codigo)
    
    # Iniciar el hilo
    hilo.start()

    # Puedes retornar una respuesta inmediata o redirigir a otra página
    return render_template('sitio/bot.html')
