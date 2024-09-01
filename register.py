from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.tab import MDTabs
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from firebase_config import db
import uuid

# Cargar el archivo KV
Builder.load_string("""
<RegisterScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        canvas.before:
            Color:
                rgba: 0.6, 0.8, 1, 1  # Celeste suave
            Rectangle:
                pos: self.pos
                size: self.size

        MDTabs:
            id: tabs

            TabCliente:
                title: 'Cliente'
                id: cliente_tab

            TabVehiculo:
                title: 'Vehículo'
                id: vehiculo_tab

            TabServicios:
                title: 'Servicios Realizados'
                id: servicios_tab

            TabFinancieros:
                title: 'Detalles Financieros'
                id: financieros_tab

            TabStock:
                title: 'Stock de Neumáticos y Accesorios'
                id: stock_tab

        MDRaisedButton:
            text: "Guardar Registro"
            size_hint_y: None
            height: dp(50)
            pos_hint: {"center_x": 0.5}
            md_bg_color: app.theme_cls.primary_color
            on_release:
                root.save_to_firestore()

        MDRaisedButton:
            text: "Volver a la Pantalla Principal"
            size_hint_y: None
            height: dp(50)
            pos_hint: {"center_x": 0.5}
            md_bg_color: app.theme_cls.primary_color
            on_release:
                root.go_to_home()

<TabCliente>:
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(10)
            padding: dp(10)

            MDTextField:
                id: client_name
                hint_text: "Nombre completo"
                required: True
                helper_text: "Ejemplo: Juan Pérez"
                helper_text_mode: "on_focus"

            MDTextField:
                id: client_contact
                hint_text: "Número de contacto"
                required: True
                input_filter: 'int'
                helper_text: "Ingrese el número sin espacios ni guiones"
                helper_text_mode: "on_focus"

            MDTextField:
                id: client_address
                hint_text: "Dirección"
                required: True
                helper_text: "Ejemplo: Calle Falsa 123"
                helper_text_mode: "on_focus"

<TabVehiculo>:
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(10)
            padding: dp(10)

            MDTextField:
                id: vehicle_type
                hint_text: "Tipo de Vehículo"
                required: True
                helper_text: "Ejemplo: Auto, Moto, Camión"
                helper_text_mode: "on_focus"

            MDTextField:
                id: vehicle_brand
                hint_text: "Marca del vehículo"
                required: True
                helper_text: "Ejemplo: Toyota"
                helper_text_mode: "on_focus"

            MDTextField:
                id: vehicle_model
                hint_text: "Modelo del vehículo"
                required: True
                helper_text: "Ejemplo: Corolla"
                helper_text_mode: "on_focus"

            MDTextField:
                id: vehicle_year
                hint_text: "Año de fabricación"
                required: True
                input_filter: 'int'
                helper_text: "Ejemplo: 2015"
                helper_text_mode: "on_focus"

            MDTextField:
                id: vehicle_plate
                hint_text: "Matrícula"
                required: True
                helper_text: "Ejemplo: ABC123"
                helper_text_mode: "on_focus"

<TabServicios>:
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(10)
            padding: dp(10)

            MDTextField:
                id: service_type
                hint_text: "Tipo de Servicio"
                required: True
                helper_text: "Ejemplo: Cambio de aceite, alineación"
                helper_text_mode: "on_focus"

            MDTextField:
                id: service_date
                hint_text: "Fecha del Servicio (DD/MM/AAAA)"
                required: True
                helper_text: "Formato: Día/Mes/Año"
                helper_text_mode: "on_focus"

            MDTextField:
                id: tire_quantity
                hint_text: "Cantidad de Neumáticos"
                required: True
                input_filter: 'int'
                helper_text: "Número total de neumáticos"
                helper_text_mode: "on_focus"

            MDTextField:
                id: tire_status_before
                hint_text: "Estado Antes del Servicio"
                required: True
                helper_text: "Condición antes del servicio"
                helper_text_mode: "on_focus"

            MDTextField:
                id: tire_status_after
                hint_text: "Estado Después del Servicio"
                required: True
                helper_text: "Condición después del servicio"
                helper_text_mode: "on_focus"

<TabFinancieros>:
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(10)
            padding: dp(10)

            MDTextField:
                id: service_cost
                hint_text: "Costo del Servicio"
                required: True
                input_filter: 'float'
                helper_text: "Ingrese el monto total en la moneda local"
                helper_text_mode: "on_focus"

            MDTextField:
                id: invoice_number
                hint_text: "Número de Factura/Recibo"
                required: True
                helper_text: "Número único para identificar el recibo"
                helper_text_mode: "on_focus"

<TabStock>:
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(10)
            padding: dp(10)

            MDTextField:
                id: tire_brand
                hint_text: "Marca del Neumático"
                required: True
                helper_text: "Ejemplo: Michelin"
                helper_text_mode: "on_focus"

            MDTextField:
                id: tire_model
                hint_text: "Modelo del Neumático"
                required: True
                helper_text: "Ejemplo: Pilot Sport"
                helper_text_mode: "on_focus"

            MDTextField:
                id: tire_size
                hint_text: "Tamaño del Neumático"
                required: True
                helper_text: "Ejemplo: 205/55 R16"
                helper_text_mode: "on_focus"

            MDTextField:
                id: tire_quantity_stock
                hint_text: "Cantidad en Stock"
                required: True
                input_filter: 'int'
                helper_text: "Número total de neumáticos en inventario"
                helper_text_mode: "on_focus"

            MDTextField:
                id: tire_entry_date
                hint_text: "Fecha de Ingreso (DD/MM/AAAA)"
                required: True
                helper_text: "Fecha en que los neumáticos ingresaron al inventario"
                helper_text_mode: "on_focus"

            MDTextField:
                id: valves_quantity
                hint_text: "Cantidad de Válvulas"
                required: True
                input_filter: 'int'
                helper_text: "Número total de válvulas en inventario"
                helper_text_mode: "on_focus"

            MDTextField:
                id: tubes_quantity
                hint_text: "Cantidad de Cámaras"
                required: True
                input_filter: 'int'
                helper_text: "Número total de cámaras en inventario"
                helper_text_mode: "on_focus"

            MDTextField:
                id: protectors_quantity
                hint_text: "Cantidad de Protectores"
                required: True
                input_filter: 'int'
                helper_text: "Número total de protectores en inventario"
                helper_text_mode: "on_focus"
""")

class TabCliente(Screen, MDTabsBase):
    def get_cliente_data(self):
        return {
            'nombre_completo': self.ids.client_name.text if self.ids.client_name.text else "N/A",
            'numero_contacto': self.ids.client_contact.text if self.ids.client_contact.text else "N/A",
            'direccion': self.ids.client_address.text if self.ids.client_address.text else "N/A",
        }

class TabVehiculo(Screen, MDTabsBase):
    def get_vehiculo_data(self):
        return {
            'tipo': self.ids.vehicle_type.text if self.ids.vehicle_type.text else "N/A",
            'marca': self.ids.vehicle_brand.text if self.ids.vehicle_brand.text else "N/A",
            'modelo': self.ids.vehicle_model.text if self.ids.vehicle_model.text else "N/A",
            'año_fabricacion': self.ids.vehicle_year.text if self.ids.vehicle_year.text else "N/A",
            'matricula': self.ids.vehicle_plate.text if self.ids.vehicle_plate.text else "N/A",
        }

class TabServicios(Screen, MDTabsBase):
    def get_servicios_data(self):
        return {
            'tipo_servicio': self.ids.service_type.text if self.ids.service_type.text else "N/A",
            'fecha_servicio': self.ids.service_date.text if self.ids.service_date.text else "N/A",
            'cantidad_neumaticos': self.ids.tire_quantity.text if self.ids.tire_quantity.text else "N/A",
            'estado_neumaticos_antes': self.ids.tire_status_before.text if self.ids.tire_status_before.text else "N/A",
            'estado_neumaticos_despues': self.ids.tire_status_after.text if self.ids.tire_status_after.text else "N/A",
        }

class TabFinancieros(Screen, MDTabsBase):
    def get_financieros_data(self):
        return {
            'costo_servicio': self.ids.service_cost.text if self.ids.service_cost.text else "N/A",
            'numero_factura': self.ids.invoice_number.text if self.ids.invoice_number.text else "N/A",
        }

class TabStock(Screen, MDTabsBase):
    def get_stock_data(self):
        return {
            'marca_neumatico': self.ids.tire_brand.text if self.ids.tire_brand.text else "N/A",
            'modelo_neumatico': self.ids.tire_model.text if self.ids.tire_model.text else "N/A",
            'tamaño_neumatico': self.ids.tire_size.text if self.ids.tire_size.text else "N/A",
            'cantidad_neumaticos_stock': self.ids.tire_quantity_stock.text if self.ids.tire_quantity_stock.text else "N/A",
            'fecha_ingreso_neumaticos': self.ids.tire_entry_date.text if self.ids.tire_entry_date.text else "N/A",
            'valvulas_cantidad': self.ids.valves_quantity.text if self.ids.valves_quantity.text else "N/A",
            'camaras_cantidad': self.ids.tubes_quantity.text if self.ids.tubes_quantity.text else "N/A",
            'protectores_cantidad': self.ids.protectors_quantity.text if self.ids.protectors_quantity.text else "N/A",
        }

class RegisterScreen(Screen):
    def save_to_firestore(self):
        try:
            cliente_tab = self.ids.cliente_tab
            vehiculo_tab = self.ids.vehiculo_tab
            servicios_tab = self.ids.servicios_tab
            financieros_tab = self.ids.financieros_tab
            stock_tab = self.ids.stock_tab

            cliente_data = cliente_tab.get_cliente_data()
            vehiculo_data = vehiculo_tab.get_vehiculo_data()
            servicios_data = servicios_tab.get_servicios_data()
            financieros_data = financieros_tab.get_financieros_data()
            stock_data = stock_tab.get_stock_data()

            incomplete_fields = []
            for tab_name, data in {"Cliente": cliente_data, "Vehículo": vehiculo_data, "Servicios": servicios_data, 
                                   "Financieros": financieros_data, "Stock": stock_data}.items():
                for key, value in data.items():
                    if not value.strip():  # Ignorar espacios en blanco
                        incomplete_fields.append(f"{key} en {tab_name}")

            if incomplete_fields:
                self.show_incomplete_fields_dialog(incomplete_fields)
                return

            cliente_id = str(uuid.uuid4())  # Generar un ID único para cada cliente

            cliente_document = {
                'cliente': cliente_data,
                'vehiculo': vehiculo_data,
                'servicios': servicios_data,
                'financieros': financieros_data,
                'stock': stock_data,
            }

            db.collection('clientes').document(cliente_id).set(cliente_document)
            print("Datos guardados en Firestore bajo el cliente:", cliente_id)
            self.clear_fields()
            self.show_confirmation_dialog()  # Mostrar el cuadro de diálogo

        except AttributeError as e:
            print(f"Error: las pestañas no contienen los elementos esperados: {e}")
        except Exception as e:
            print(f"Error al guardar en Firestore: {e}")

    def show_incomplete_fields_dialog(self, fields):
        fields_str = '\n'.join(fields)
        dialog = MDDialog(
            title="Campos Incompletos",
            text=f"Por favor, completa los siguientes campos:\n{fields_str}",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def clear_fields(self):
        for tab in [self.ids.cliente_tab, self.ids.vehiculo_tab, self.ids.servicios_tab, self.ids.financieros_tab, self.ids.stock_tab]:
            for child in tab.ids.values():
                if isinstance(child, MDTextField):
                    child.text = ""

    def show_confirmation_dialog(self):
        dialog = MDDialog(
            title="Registro Guardado",
            text="Los datos se han guardado correctamente.",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_home(self):
        # Cambiar la pantalla activa al 'home_screen'
        self.manager.current = 'home_screen'