import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1960, 960
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Novela Gráfica Undercaves")

def load_image(name):
    try:
        image = pygame.image.load(name)
        return pygame.transform.scale(image, (WIDTH, HEIGHT))
    except pygame.error as e:
        print(f"Error al cargar la imagen {name}: {e}")
        return None

images = {
    "img_inicial": load_image("0.png"),
    "img_cueva": load_image("1.png"),
    "img_prota": load_image("2.png"),
    "img_ciudad": load_image("3.png"),
    "img_puesto": load_image("4.png"),
    "img_castillo": load_image("5.png"),
    "img_monstruo_de_caballeria": load_image("6.png"),
    "img_espada_legendaria": load_image("7.png"),
    "img_monstruo_boss": load_image("8.png"),
    "img_monstruo_boss_2": load_image("10.png"),
    "img_boss_caballero_monstruo": load_image("11.png"),
    "img_los_caballeros_del_destino": load_image("12.png"),
    "img_boss_final_caballero_obscuro": load_image("13.png"),
    "img_campo_de_batalla_final": load_image("14.png")
}

# Fuente de texto
font = pygame.font.Font(None, 30)

def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

class GameState:
    def __init__(self):
        self.state = "Iniciar el Crono"
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.handle_key_1()
            elif event.key == pygame.K_2:
                self.handle_key_2()
    
    def handle_key_1(self):
        if self.state == "Iniciar el Crono":
            self.state = "buscar una salida"
        elif self.state == "buscar una salida":
            self.state = "Rendirte ante el frio"
        elif self.state == "Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)":
            self.state = "Ir hacia la luz"
        elif self.state == "Rendirte ante el frio":
            self.state = "Moriste congelado"
        elif self.state == "Ir hacia la luz":
            self.state = "Ir a comer algo al puesto de comida"
        elif self.state == "Ir a comer algo al puesto de comida":
            self.state = "Fuiste a comer al puesto de comida, eventualmente te sentiste mal y explotaste."
        elif self.state == "Ir hacia el castillo a investigar sobre el pueblo":
            self.state = "Hablar con el monstruo"
        elif self.state == "Hablar con el monstruo":
            self.state = "Ayudar con la profesia"
        elif self.state == "Ayudar con la profesia":
            self.state = "Ir hacia el rey"
        elif self.state == "Ir hacia el rey":
            self.state = "Continuar tu camino"
        elif self.state == "Continuar tu camino":
            self.state = "Esperar al rey"
        elif self.state == "Esperar al rey":
            self.state = "Ayudar a eliminar la corrupción"
        elif self.state == "Ayudar a eliminar la corrupción":
            self.state = "Ir a cumplir tu mision..."
        elif self.state == "Ir a cumplir tu mision...":
            self.state = "Proclamarse vicrtorioso..."
        elif self.state == "Proclamarse vicrtorioso...":
            self.state = "Legendary Ending. Victoria..."
        elif self.state == "Retroceder para buscar la salida":
            self.state = "Aceptar su invitacion"
        elif self.state == "Aceptar su invitacion":
            self.state = "Sientes como se consume tu alma, el caballero se hace mas poderoso..."

    def handle_key_2(self):
        if self.state == "Iniciar el Crono":
            self.state = "Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)"
        elif self.state == "buscar una salida":
            self.state = "Seguir buscando una salida"
        elif self.state == "Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)":
            self.state = "Retroceder para buscar la salida"
        elif self.state == "Ir hacia la luz":
            self.state = "Ir hacia el castillo a investigar sobre el pueblo"
        elif self.state == "Ir hacia el castillo a investigar sobre el pueblo":
            self.state = "Intentar pelear con el con tus habilidades mágicas"
        elif self.state == "Intentar pelear con el con tus habilidades mágicas":
            self.state = "El monstruo acabó contigo en tan solo un movimiento de brazo, patético"
        elif self.state == "Hablar con el monstruo":
            self.state = "Irse del lugar"
        elif self.state == "Irse del lugar":
            self.state = "Decides irte sin embargo el monstruo te ataca con su arma atravesándote"
        elif self.state == "Esperar al rey":
            self.state = "Negarse ya que no tienes nada que ver con ese reino"
        elif self.state == "Negarse ya que no tienes nada que ver con ese reino":
            self.state = "Al escuchar esto el rey le ordena a tu guardia de tu ejecucion"
        elif self.state == "Seguir buscando una salida":
            self.state = "A pesar de tu desespere de buscar la salida te perdiste en el vacio de la fronteras"
        elif self.state == "Retroceder para buscar la salida":
            self.state = "Caballero desconocido: hey, que haces aca pequeño humano?"
        elif self.state == "Retroceder para buscar la salida":
            self.state = "Rechazar su oferta"
        elif self.state == "Rechazar su oferta":
            self.state = "Ah, es una lastima, total iba a consumir tu alma..."

    def show(self):
        screen.fill(BLACK)
        if self.state == "Iniciar el Crono":
            if images["img_inicial"]:
                screen.blit(images["img_inicial"], (0, 0))
            draw_text("Caíste de una altura muy alta, estás conmocionado y parece que estás herido internamente", 430, 300)
            draw_text("Recuerdas quién eres de golpe, Zhongli, exacto, eres el héroe legendario de la superficie", 430, 330)
            draw_text("Zhongli: claro, ahora lo recuerdo, estaba de expedición cuando una brecha de portal", 430, 360)
            draw_text("me absorbió al sub-suelo, es bastante diferente a las leyendas...", 430, 390)
            draw_text("Zhongli: Bueno, será mejor que comience a caminar por acá, hace frío a decir verdad...", 430, 420)
            draw_text("Opciones del destino", 450, 500)
            draw_text("1. Buscar una salida", 450, 550)
            draw_text("2. Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)", 450, 600)
        elif self.state == "buscar una salida":
            if images["img_cueva"]:
                screen.blit(images["img_cueva"], (0, 0))
            draw_text("Te perdiste buscando la salida, sientes el frío comenzando a afectarte poco a poco...", 430, 100)
            draw_text("1. Rendirte ante el frío", 450, 150)
            draw_text("2. Seguir buscando una salida", 450, 200)
        elif self.state == "Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)":
            if images["img_cueva"]:
                screen.blit(images["img_cueva"], (0, 0))
            draw_text("Ves una luz al final del túnel, deseas ir hacia ella?", 430, 100)
            draw_text("1. Ir hacia la luz", 450, 150)
            draw_text("2. Retroceder para buscar la salida", 450, 200)
        elif self.state == "Rendirte ante el frío":
            draw_text("Moriste congelado", 450, 450)
        elif self.state == "Seguir buscando una salida":
            if images["img_cueva"]:
                screen.blit(images["img_cueva"], (0, 0))
            draw_text("A pesar de tu desespere de buscar la salida te perdiste en el vacio de la fronteras", 550, 100)
            draw_text("Sientes como la obscuridad te consume tu alma y finalmente te dejas consumir...", 550, 150)
        elif self.state == "Rechazar su oferta":
            if images["img_boss_final_caballero_obscuro"]:
                screen.blit(images["img_boss_final_caballero_obscuro"], (0, 0))
            draw_text("Ah, es una lastima, total iba a consumir tu alma...", 550, 100)
            draw_text("Qu-", 550, 150)
            draw_text("El caballero te atraveso robandote el alma...", 550, 200)
        elif self.state == "Ir hacia la luz":
            if images["img_ciudad"]:
                screen.blit(images["img_ciudad"], (0, 0))
            draw_text("Caes encima de la ciudad, es enorme y repleta de monstruos como personas, ves un puesto", 430, 100)
            draw_text("de comida a lo lejos y un castillo algo tétrico", 430, 150)
            draw_text("1. Ir a comer algo al puesto de comida", 450, 250)
            draw_text("2. Ir hacia el castillo a investigar sobre el pueblo", 450, 300)
        elif self.state == "Retroceder para buscar la salida":
            if images["img_boss_final_caballero_obscuro"]:
                screen.blit(images["img_boss_final_caballero_obscuro"], (0, 0))
            draw_text("Caballero desconocido: hey, que haces aca pequeño humano?", 550, 100)
            draw_text("Zhongli: e-eh nada, justo me estaba por ir, adios", 550, 150)
            draw_text("Nah, tu no te vas... unete a mi chico, hazme caso...", 550, 200)
            draw_text("1. Aceptar su invitacion", 550, 300)
            draw_text("2. Rechazar su oferta", 550, 350)
        elif self.state == "Aceptar su invitacion":
            if images["img_boss_final_caballero_obscuro"]:
                screen.blit(images["img_boss_final_caballero_obscuro"], (0, 0))
            draw_text("Sientes como se consume tu alma, el caballero se hace mas poderoso...", 550, 100)
        elif self.state == "Ir a comer algo al puesto de comida":
            if images["img_puesto"]:
                screen.blit(images["img_puesto"], (0, 0))
            draw_text("Fuiste a comer al puesto de comida, eventualmente te sentiste mal y explotaste.", 450, 100)
        elif self.state == "Ir hacia el castillo a investigar sobre el pueblo":
            if images["img_castillo"]:
                screen.blit(images["img_castillo"], (0, 0))
            draw_text("Llegaste al castillo, es inmenso y repleto de estatuas en forma de monstruos", 450, 100)
            draw_text("Encuentras un monstruo de caballería", 450, 150)
            draw_text("1. Hablar con el monstruo", 450, 200)
            draw_text("2. Intentar pelear con el con tus habilidades mágicas", 450, 250)
        elif self.state == "Hablar con el monstruo":
            if images["img_monstruo_de_caballeria"]:
                screen.blit(images["img_monstruo_de_caballeria"], (0, 0))
            draw_text("Te acercas para hablar con el monstruo, en tu plática te habla del reino Puertero: Este reino se formó hace ", 550, 100)
            draw_text(" *ilegible* años, todo era pacífico hasta que el vacío se apoderó de las fronteras del reino", 550, 150)
            draw_text("Según la profecía un guerrero de aura carmesí nos librará de este fatídico final, y tal parece que ese eres tú.", 550, 200)
            draw_text("Zhongli: ¿YO!? ¿De qué hablas? soy un héroe de la superficie no de las catacumbas del sub-suelo", 550, 250)
            draw_text("1. Ayudar con la profesia", 600, 350)
            draw_text("2. Irse del lugar", 600, 400)
        elif self.state == "Intentar pelear con el con tus habilidades mágicas":
            draw_text("El monstruo acabó contigo en tan solo un movimiento de brazo, patético", 450, 350)
        elif self.state == "Irse del lugar":
            draw_text("Decides irte sin embargo el monstruo te ataca con su arma atravesándote", 500, 100)
        elif self.state == "Ayudar con la profesia":
            if images["img_espada_legendaria"]:
                screen.blit(images["img_espada_legendaria"], (0, 0))
            draw_text("Perfecto, pasa adelante, mi rey te espera dentro, antes toma esto, *espada legendaria*", 550, 200)
            draw_text("1. Ir hacia el rey", 600, 300)
        elif self.state == "Ir hacia el rey":
            if images["img_monstruo_boss"]:
                screen.blit(images["img_monstruo_boss"], (0, 0))
            draw_text("Vaya, ¿un mortal? *voz misteriosa*", 550, 100)
            draw_text("Zhongli: ¿dónde estás?", 550, 150)
            draw_text("El monstruo se te abalanza encima intentando comerte de un mordisco", 550, 200)
            draw_text("Tu espada actúa por sí sola y lo taja a la mitad", 550, 250)
            draw_text("Zhongli: wow, eso fue inesperado...", 550, 300)
            draw_text("1. Continuar tu camino", 600, 400)
        elif self.state == "Continuar tu camino":
            if images["img_boss_caballero_monstruo"]:
                screen.blit(images["img_boss_caballero_monstruo"], (0, 0))
            draw_text("Llegas a una sala con un trono, de repente aparece una figura monstruosa", 550, 100)
            draw_text("Guardia del rey: Me presento, soy Tag, el guardia del rey, le pido que lo espere", 550, 150)
            draw_text("1. Esperar al rey", 600, 250)
        elif self.state == "Esperar al rey":
            if images["img_monstruo_boss_2"]:
                screen.blit(images["img_monstruo_boss_2"], (0, 0))
            draw_text("Bueno, me presento, soy el rey del reino del sub-suelo, CAERLEON y estás acá porque lo quiero", 550, 100)
            draw_text("Quiero que derrotes al caballero oscuro para librarnos de la corrupción.", 550, 150)
            draw_text("1. Ayudar a eliminar la corrupción", 550, 250)
            draw_text("2. Negarse ya que no tienes nada que ver con ese reino", 550, 300)
        elif self.state == "Ayudar a eliminar la corrupción":
            if images["img_los_caballeros_del_destino"]:
                screen.blit(images["img_los_caballeros_del_destino"], (0, 0))
            draw_text("El rey te otorga la energia de unos heroes miticos del sub-suelo...", 550, 100)
            draw_text("Rey: esta es la energia de unos heroes del pasado, los destinados a vencerlo a el...", 550, 150)
            draw_text("Te perturba que de pronto todo fuera tan serio pero sigues tu travesia", 550, 200)
            draw_text("1. Ir a cumplir tu mision...", 550, 300)
        elif self.state == "Negarse ya que no tienes nada que ver con ese reino":
            draw_text("Al escuchar esto el rey le ordena a tu guardia de tu ejecucion", 550, 100)
            draw_text("Intentas defenderte, sin embargo, te aniquila facilmente...", 550, 150)
        elif self.state == "Ir a cumplir tu mision...":
            if images["img_boss_final_caballero_obscuro"]:
                screen.blit(images["img_boss_final_caballero_obscuro"], (0, 0 ))
            draw_text("Caballero: Con que... tu eres zhongli...", 550, 100)
            draw_text("Zhongli: Eh? de donde saliste? *Se parece al que me encargaron matar...*", 550, 150)
            draw_text("El caballero te embiste con un ataque devastador...", 550, 200)
            draw_text("su batalla dura horas, sin embargo te declaras victorioso...", 550, 250)
            draw_text("1. Proclamarse vicrtorioso...", 600, 600)
        elif self.state == "Proclamarse vicrtorioso...":
            if images["img_campo_de_batalla_final"]:
                screen.blit(images["img_campo_de_batalla_final"], (0, 0))
            draw_text("Legendary Ending. Victoria...", 600, 600)

        pygame.display.update()

def game():
    game_state = GameState()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            game_state.handle_event(event)
        
        game_state.show()
        pygame.display.flip()

game()