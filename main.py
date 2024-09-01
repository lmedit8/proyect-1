from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.image import Image
from kivymd.uix.list import OneLineIconListItem
from register import RegisterScreen 
from firebase_config import db  # Asegúrate de importar db
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

# Establecer las dimensiones de la ventana
Window.size = (360, 640)

# Cargar el archivo KV para la pantalla principal
Builder.load_string("""
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        canvas.before:
            Color:
                rgba: [13/255, 155/255, 203/255, 1]
            Rectangle:
                pos: self.pos
                size: self.size

        Image:
            source: 'assets/Logo.jpg'
            size_hint: (1, 1)  # La imagen ocupa el 60% del ancho y alto disponibles
            pos_hint: {"center_x": 0.5, "center_y": 0.5}  # Centramos la imagen
            allow_stretch: True
            keep_ratio: True
 
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)  # Altura de los botones

            MDRaisedButton:
                text: "Inicio"
                size_hint: (0.3, 1)  # Botones más pequeños y centrados horizontalmente
                md_bg_color: app.theme_cls.primary_color
                pos_hint: {"center_x": 0.5}
                on_release:
                    app.root.current = 'home_screen'

<HomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        canvas.before:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)  # Altura de los botones

            MDRaisedButton:
                text: "Ver Registros"
                size_hint: (0.3, 1)  # Botones más pequeños y centrados horizontalmente
                md_bg_color: app.theme_cls.primary_color
                pos_hint: {"center_x": 0.5}
                on_release:
                    app.root.current = 'view_records'

            MDRaisedButton:
                text: "Crear Nuevo Registro"
                size_hint: (0.3, 1)  # Botones más pequeños y centrados horizontalmente
                md_bg_color: app.theme_cls.primary_color
                pos_hint: {"center_x": 0.5}
                on_release:
                    app.root.current = 'create_records'

<ViewRecordsScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        canvas.before:
            Color:
                rgba: app.theme_cls.primary_color  # Mismo color de fondo que en la ventana principal
            Rectangle:
                pos: self.pos
                size: self.size

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(150)
            padding: dp(10)
            spacing: dp(10)
            canvas.before:
                Color:
                    rgba: app.theme_cls.primary_color  # Fondo igual que la ventana
                Rectangle:
                    pos: self.pos
                    size: self.size

            MDLabel:
                text: "REGISTROS"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1  # Blanco para contrastar con el fondo
                font_style: "H4"
                size_hint_y: None
                height: self.texture_size[1]
                halign: "center"
                bold: True

        MDScrollView:
            id: scroll_view
            MDList:
                id: client_list

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)  # Altura de los botones
            padding: dp(10)
            spacing: dp(10)

            MDRaisedButton:
                text: "Volver"
                size_hint: (1, 1)
                md_bg_color: app.theme_cls.primary_color
                pos_hint: {"center_x": 0.5}
                on_release:
                    app.root.current = 'home_screen'

<ClientDetailsScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)
        canvas.before:
            Color:
                rgba: 0.98, 0.98, 0.98, 1  # Fondo claro
            Rectangle:
                pos: self.pos
                size: self.size

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(150)
            padding: dp(10)
            spacing: dp(10)
            canvas.before:
                Color:
                    rgba: app.theme_cls.primary_color
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(20), dp(20), dp(0), dp(0)]

            MDLabel:
                text: "REGISTRO"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1  # Blanco
                font_style: "H4"
                size_hint_y: None
                height: self.texture_size[1]
                halign: "center"
                bold: True

            MDLabel:
                id: client_name_label
                text: "Detalles del Cliente"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1  # Blanco
                font_style: "H5"
                size_hint_y: None
                height: self.texture_size[1]
                halign: "center"
                bold: True

        MDScrollView:
            id: scroll_view
            MDList:
                id: client_details_list

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            padding: dp(10)
            spacing: dp(10)

            MDRaisedButton:
                text: "Volver"
                size_hint: (0.3, 1)
                md_bg_color: app.theme_cls.primary_color
                pos_hint: {"center_x": 0.5}
                on_release:
                    app.root.current = 'view_records'

            MDRaisedButton:
                text: "Modificar"
                size_hint: (0.3, 1)
                md_bg_color: app.theme_cls.primary_color
                pos_hint: {"center_x": 0.5}
                on_release:
                    root.modify_client_details()

            MDRaisedButton:
                text: "Eliminar"
                size_hint: (0.3, 1)
                md_bg_color: app.theme_cls.error_color
                pos_hint: {"center_x": 0.5}
                on_release:
                    root.delete_client()

<ModifyRecordsScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        # Título centrado
        MDLabel:
            text: "MODIFICAR REGISTRO"
            font_style: "H5"
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]

        # ScrollView para campos de entrada
        ScrollView:
            size_hint: (1, 0.8)  # Ocupa el 80% del alto de la pantalla
            do_scroll_x: False
            do_scroll_y: True
            bar_width: dp(10)

            GridLayout:
                cols: 1
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None  # Necesario para que ScrollView funcione
                height: self.minimum_height  # Ajusta la altura del GridLayout automáticamente
                width: self.parent.width

                MDTextField:
                    id: client_name
                    hint_text: "Nombre Completo"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: contact_number
                    hint_text: "Número de Contacto"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: address
                    hint_text: "Dirección"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: vehicle_brand
                    hint_text: "Marca del Vehículo"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: vehicle_model
                    hint_text: "Modelo del Vehículo"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: manufacture_year
                    hint_text: "Año de Fabricación"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: license_plate
                    hint_text: "Matrícula"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: service_type
                    hint_text: "Tipo de Servicio"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: service_date
                    hint_text: "Fecha del Servicio"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: tire_quantity
                    hint_text: "Cantidad de Neumáticos"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: tire_condition_before
                    hint_text: "Estado de Neumáticos Antes"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: tire_condition_after
                    hint_text: "Estado de Neumáticos Después"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: service_cost
                    hint_text: "Costo del Servicio"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: invoice_number
                    hint_text: "Número de Factura"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: tire_brand
                    hint_text: "Marca de Neumático"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: tire_model
                    hint_text: "Modelo de Neumático"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: tire_size
                    hint_text: "Tamaño del Neumático"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: tire_stock
                    hint_text: "Cantidad en Stock"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: stock_entry_date
                    hint_text: "Fecha de Ingreso"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: valve_quantity
                    hint_text: "Cantidad de Válvulas"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: tube_quantity
                    hint_text: "Cantidad de Cámaras"
                    size_hint_y: None
                    height: dp(40)

                MDTextField:
                    id: protector_quantity
                    hint_text: "Cantidad de Protectores"
                    size_hint_y: None
                    height: dp(40)

        # Botones centrados
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            spacing: dp(20)
            padding: [0, dp(10), 0, 0]
            pos_hint: {"center_x": .5}

            MDRaisedButton:
                text: "Guardar"
                size_hint_x: None
                width: dp(100)
                on_release: root.save_modified_data()

            MDRaisedButton:
                text: "Cancelar"
                size_hint_x: None
                width: dp(100)
                on_release: app.root.current = 'client_details_screen'


""")


# Definición de pantallas y widgets
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        logo = Image(source='assets/Logo.jpg', size_hint=(0.6, 0.6), allow_stretch=True, keep_ratio=True)
        logo.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        button_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        button_box.add_widget(MDRaisedButton(text="Inicio", on_release=self.go_to_home, size_hint=(0.3, 1)))

        layout.add_widget(logo)
        layout.add_widget(button_box)

        self.add_widget(layout)

    def go_to_home(self, instance):
        self.manager.current = 'home_screen'


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        button_box1 = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        button_box1.add_widget(MDRaisedButton(text="Ver Registros", on_release=self.go_to_view_records, size_hint=(0.3, 1)))

        button_box2 = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        button_box2.add_widget(MDRaisedButton(text="Crear Nuevo Registro", on_release=self.go_to_create_record, size_hint=(0.3, 1)))

        layout.add_widget(button_box1)
        layout.add_widget(button_box2)

        self.add_widget(layout)

    def go_to_view_records(self, instance):
        self.manager.current = 'view_records'

    def go_to_create_record(self, instance):
        self.manager.current = 'create_records'

class ViewRecordsScreen(Screen):
    def on_pre_enter(self, *args):
        # Este método se llama antes de que la pantalla se vuelva visible.
        self.load_clients()

    def load_clients(self):
        self.ids.client_list.clear_widgets()
        clients_ref = db.collection('clientes')
        docs = clients_ref.stream()

        for doc in docs:
            client_name = doc.to_dict().get('cliente', {}).get('nombre_completo', 'No Name')
            item = OneLineIconListItem(text=client_name, on_release=self.show_client_details)
            item.client_id = doc.id  # Store client ID in item
            self.ids.client_list.add_widget(item)

    def show_client_details(self, instance):
        client_id = instance.client_id
        self.manager.current = 'client_details_screen'
        self.manager.get_screen('client_details_screen').load_client_details(client_id)

    def go_back(self):
        self.manager.current = 'home_screen'


class ClientDetailsScreen(Screen):

    def load_client_details(self, client_id):
        self.client_id = client_id  # Almacenar el ID del cliente
        self.ids.client_details_list.clear_widgets()
        client_ref = db.collection('clientes').document(client_id)
        client_doc = client_ref.get()

        if client_doc.exists:
            client_data = client_doc.to_dict()
            cliente = client_data.get('cliente', {})
            vehiculo = client_data.get('vehiculo', {})
            servicios = client_data.get('servicios', {})
            financieros = client_data.get('financieros', {})
            stock = client_data.get('stock', {})

            details = {
                'Nombre Completo': cliente.get('nombre_completo', 'N/A'),
                'Número de Contacto': cliente.get('numero_contacto', 'N/A'),
                'Dirección': cliente.get('direccion', 'N/A'),
                'Marca del Vehículo': vehiculo.get('marca', 'N/A'),
                'Modelo del Vehículo': vehiculo.get('modelo', 'N/A'),
                'Año de Fabricación': vehiculo.get('año_fabricacion', 'N/A'),
                'Matrícula': vehiculo.get('matricula', 'N/A'),
                'Tipo de Servicio': servicios.get('tipo_servicio', 'N/A'),
                'Fecha del Servicio': servicios.get('fecha_servicio', 'N/A'),
                'Cantidad de Neumáticos': servicios.get('cantidad_neumaticos', 'N/A'),
                'Estado de Neumáticos Antes': servicios.get('estado_neumaticos_antes', 'N/A'),
                'Estado de Neumáticos Después': servicios.get('estado_neumaticos_despues', 'N/A'),
                'Costo del Servicio': financieros.get('costo_servicio', 'N/A'),
                'Número de Factura': financieros.get('numero_factura', 'N/A'),
                'Marca de Neumático': stock.get('marca_neumatico', 'N/A'),
                'Modelo de Neumático': stock.get('modelo_neumatico', 'N/A'),
                'Tamaño del Neumático': stock.get('tamaño_neumatico', 'N/A'),
                'Cantidad en Stock': stock.get('cantidad_neumaticos_stock', 'N/A'),
                'Fecha de Ingreso': stock.get('fecha_ingreso_neumaticos', 'N/A'),
                'Cantidad de Válvulas': stock.get('valvulas_cantidad', 'N/A'),
                'Cantidad de Cámaras': stock.get('camaras_cantidad', 'N/A'),
                'Cantidad de Protectores': stock.get('protectores_cantidad', 'N/A'),
            }

            for key, value in details.items():
                self.ids.client_details_list.add_widget(OneLineIconListItem(text=f"{key}: {value}"))

    def modify_client_details(self):
        modify_screen = self.manager.get_screen('modify_records_screen')
        client_ref = db.collection('clientes').document(self.client_id)
        client_doc = client_ref.get()

        if client_doc.exists:
            client_data = client_doc.to_dict()
            cliente = client_data.get('cliente', {})
            vehiculo = client_data.get('vehiculo', {})
            servicios = client_data.get('servicios', {})
            financieros = client_data.get('financieros', {})
            stock = client_data.get('stock', {})

            modify_screen.ids.client_name.text = cliente.get('nombre_completo', '')
            modify_screen.ids.contact_number.text = cliente.get('numero_contacto', '')
            modify_screen.ids.address.text = cliente.get('direccion', '')
            modify_screen.ids.vehicle_brand.text = vehiculo.get('marca', '')
            modify_screen.ids.vehicle_model.text = vehiculo.get('modelo', '')
            modify_screen.ids.manufacture_year.text = vehiculo.get('año_fabricacion', '')
            modify_screen.ids.license_plate.text = vehiculo.get('matricula', '')
            modify_screen.ids.service_type.text = servicios.get('tipo_servicio', '')
            modify_screen.ids.service_date.text = servicios.get('fecha_servicio', '')
            modify_screen.ids.tire_quantity.text = servicios.get('cantidad_neumaticos', '')
            modify_screen.ids.tire_condition_before.text = servicios.get('estado_neumaticos_antes', '')
            modify_screen.ids.tire_condition_after.text = servicios.get('estado_neumaticos_despues', '')
            modify_screen.ids.service_cost.text = financieros.get('costo_servicio', '')
            modify_screen.ids.invoice_number.text = financieros.get('numero_factura', '')
            modify_screen.ids.tire_brand.text = stock.get('marca_neumatico', '')
            modify_screen.ids.tire_model.text = stock.get('modelo_neumatico', '')
            modify_screen.ids.tire_size.text = stock.get('tamaño_neumatico', '')
            modify_screen.ids.tire_stock.text = stock.get('cantidad_neumaticos_stock', '')
            modify_screen.ids.stock_entry_date.text = stock.get('fecha_ingreso_neumaticos', '')
            modify_screen.ids.valve_quantity.text = stock.get('valvulas_cantidad', '')
            modify_screen.ids.tube_quantity.text = stock.get('camaras_cantidad', '')
            modify_screen.ids.protector_quantity.text = stock.get('protectores_cantidad', '')

        self.manager.current = 'modify_records_screen'

    def delete_client(self):
        # Mostrar una alerta de confirmación antes de eliminar
        confirm_dialog = MDDialog(
            title="Confirmar eliminación",
            text="¿Estás seguro de que deseas eliminar este cliente?",
            buttons=[
                MDFlatButton(
                    text="CANCELAR",
                    on_release=lambda x: confirm_dialog.dismiss()
                ),
                MDRaisedButton(
                    text="ELIMINAR",
                    on_release=lambda x: self.confirm_delete_client(confirm_dialog)
                ),
            ],
        )
        confirm_dialog.open()

    def confirm_delete_client(self, dialog):
        # Eliminar cliente si el usuario confirma la acción
        dialog.dismiss()  # Cerrar el cuadro de diálogo de confirmación
        db.collection('clientes').document(self.client_id).delete()
        self.manager.get_screen('view_records').load_clients()  # Actualizar la lista de clientes
        self.manager.current = 'view_records'


class ModifyRecordsScreen(Screen):
    def save_modified_data(self):
        # Obtener el ID del cliente desde la pantalla de detalles
        client_id = self.manager.get_screen('client_details_screen').client_id

        # Recopilar los datos modificados
        modified_data = {
            'cliente': {
                'nombre_completo': self.ids.client_name.text,
                'numero_contacto': self.ids.contact_number.text,
                'direccion': self.ids.address.text,
                'marca': self.ids.vehicle_brand.text,
                'modelo': self.ids.vehicle_model.text,
                'año_fabricacion': self.ids.manufacture_year.text,
                'matricula': self.ids.license_plate.text,
            },
            'servicios': {
                'tipo_servicio': self.ids.service_type.text,
                'fecha_servicio': self.ids.service_date.text,
                'cantidad_neumaticos': self.ids.tire_quantity.text,
                'estado_neumaticos_antes': self.ids.tire_condition_before.text,
                'estado_neumaticos_despues': self.ids.tire_condition_after.text,
            },
            'financieros': {
                'costo_servicio': self.ids.service_cost.text,
                'numero_factura': self.ids.invoice_number.text,
            },
            'stock': {
                'marca_neumatico': self.ids.tire_brand.text,
                'modelo_neumatico': self.ids.tire_model.text,
                'tamaño_neumatico': self.ids.tire_size.text,
                'cantidad_neumaticos_stock': self.ids.tire_stock.text,
                'fecha_ingreso_neumaticos': self.ids.stock_entry_date.text,
                'valvulas_cantidad': self.ids.valve_quantity.text,
                'camaras_cantidad': self.ids.tube_quantity.text,
                'protectores_cantidad': self.ids.protector_quantity.text,
            }
        }

        # Actualizar los datos en Firestore
        db.collection('clientes').document(client_id).set(modified_data, merge=True)

        # Regresar a la pantalla de detalles del cliente y actualizar los detalles
        client_details_screen = self.manager.get_screen('client_details_screen')
        client_details_screen.load_client_details(client_id)
        self.manager.current = 'client_details_screen'


class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(HomeScreen(name='home_screen'))
        sm.add_widget(ViewRecordsScreen(name='view_records'))
        sm.add_widget(ClientDetailsScreen(name='client_details_screen'))
        sm.add_widget(ModifyRecordsScreen(name='modify_records_screen'))
        sm.add_widget(RegisterScreen(name='create_records'))
        return sm

if __name__ == '__main__':
    MyApp().run()