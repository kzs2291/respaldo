#carga de datos iniciales de trabajo


list_usuarios=[
    {        
        "USUARIO_EMAIL" : "prueba1@gmail.com",
        "USUARIO_PASSWORD":"123",
        "USUARIO_IS_ACTIVE": "True" 
        },
    {        
        "USUARIO_EMAIL" : "prueba2@gmail.com",
        "USUARIO_PASSWORD": "123",
        "USUARIO_IS_ACTIVE": "True"
        },
]

list_empresa=[
    {       
        "EMPRESA_NOMBRE":"compania demo" ,
        "EMPRESA_UBICACION":"provincia demo" ,
        "EMPRESA_TELEFONO":"8888 9999" ,
        "EMPRESA_CELULAR":"9999 8888" ,
        "EMPRESA_DESCRIPCION":"del palo de mango 500 varas" ,
        "EMPRESA_LATITUD":"10 10 10" ,
        "EMPRESA_LONGITUD":"20 20 20" ,
        "EMPRESA_OTROS":"por si acaso" ,
        "EMPRESA_FOTO_FONDO":".//fotos/principal.jpg",
        "EMPRESA_LOGO":"..//fotos/logo.jpg" 
    }
]

list_anuncios=[
    {
        
        "ANUNCIO_NOMBRE" :"inicio de Yoga",
        "ANUNCIO_DESCRIPCION" :"gran apertura de yoga, primera clase gratis, costo por clase 5000 colones",
        "ANUNCIO_FOTO_FONDO": "..//fotos/anuncio_yoga.jpg",
        "EMPRESA_ID" : 1
      
    },
    {
        
        "ANUNCIO_NOMBRE" :"inicio de Spinning",
        "ANUNCIO_DESCRIPCION" :" primera clase gratis, costo por clase 4000 colones",
        "ANUNCIO_FOTO_FONDO": "..//fotos/anuncio_spinning.jpg",
        "EMPRESA_ID" : 1
      
    }

]

list_actividades=[
    {
       
        "ACTIVIDAD_NOMBRE":"kempo",
        "ACTIVIDAD_ENTRENADOR":"mr Popo",
        "ACTIVIDAD_LUGAR" : "templo sagrada kamizama",
        "ACTIVIDAD_PRECIO" :0,
        "ACTIVIDAD_ESPACIOS" :10,
        "ACTIVIDAD_ESPACIOS_DISPONIBLES" : 10,
        "ACTIVIDAD_DESCRIPCION" :"conozca las ultimas tecnicas sagradas de kami",
        "ACTIVIDAD_ESTADO" :"Publicada",
        "ACTIVIDAD_DIA_SEMANA" :"Lunes",
        "ACTIVIDAD_FECHA_INICIO" : "2021-05-03",
        "ACTIVIDAD_HORA_INICIO" :"20:00",
        "ACTIVIDAD_DURACION" :60,
        "ACTIVIDAD_FOTO" :"..//fotos/actividad_kempo.jpg",
        "EMPRESA_ID" :1
    },
  
    {
       
        "ACTIVIDAD_NOMBRE":"yoga",
        "ACTIVIDAD_ENTRENADOR":"sadguru",
        "ACTIVIDAD_LUGAR" : "sabana",
        "ACTIVIDAD_PRECIO" :5000,
        "ACTIVIDAD_ESPACIOS" :10,
        "ACTIVIDAD_ESPACIOS_DISPONIBLES" : 10,
        "ACTIVIDAD_DESCRIPCION" :"conozca las ultimas tecnicas meditacion",
        "ACTIVIDAD_ESTADO" :"Publicada",
        "ACTIVIDAD_DIA_SEMANA" :"Lunes",
        "ACTIVIDAD_FECHA_INICIO" : "2021-05-03",
        "ACTIVIDAD_HORA_INICIO" :"19:00",
        "ACTIVIDAD_DURACION" :60,
        "ACTIVIDAD_FOTO" :"..//fotos/actividad_yoga.jpg",
        "EMPRESA_ID" :1
    },

     {
       
        "ACTIVIDAD_NOMBRE":"Crossfit",
        "ACTIVIDAD_ENTRENADOR":"Arnold S",
        "ACTIVIDAD_LUGAR" : "Salon principal",
        "ACTIVIDAD_PRECIO" :7000,
        "ACTIVIDAD_ESPACIOS" :10,
        "ACTIVIDAD_ESPACIOS_DISPONIBLES" : 10,
        "ACTIVIDAD_DESCRIPCION" :"conozca las ultimas tecnicas meditacion",
        "ACTIVIDAD_ESTADO" :"Publicada",
        "ACTIVIDAD_DIA_SEMANA" :"Martes",
        "ACTIVIDAD_FECHA_INICIO" : "2021-05-04",
        "ACTIVIDAD_HORA_INICIO" :"13:00",
        "ACTIVIDAD_DURACION" :90,
        "ACTIVIDAD_FOTO" :"..//fotos/actividad_Crossfit.jpg",
        "EMPRESA_ID" :1
    },
]