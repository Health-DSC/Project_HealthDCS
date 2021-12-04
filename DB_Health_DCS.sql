-- we don't know how to generate root <with-no-name> (class Root) :(

create table auth_group
(
    id   int auto_increment
        primary key,
    name varchar(150) not null,
    constraint name
        unique (name)
);

create table auth_user
(
    id           int auto_increment
        primary key,
    password     varchar(128) not null,
    last_login   datetime(6)  null,
    is_superuser tinyint(1)   not null,
    username     varchar(150) not null,
    first_name   varchar(30)  not null,
    last_name    varchar(150) not null,
    email        varchar(254) not null,
    is_staff     tinyint(1)   not null,
    is_active    tinyint(1)   not null,
    date_joined  datetime(6)  not null,
    constraint username
        unique (username)
);

create table auth_user_groups
(
    id       int auto_increment
        primary key,
    user_id  int not null,
    group_id int not null,
    constraint auth_user_groups_user_id_group_id_94350c0c_uniq
        unique (user_id, group_id),
    constraint auth_user_groups_group_id_97559544_fk_auth_group_id
        foreign key (group_id) references auth_group (id),
    constraint auth_user_groups_user_id_6a12ed8b_fk_auth_user_id
        foreign key (user_id) references auth_user (id)
);

create table django_content_type
(
    id        int auto_increment
        primary key,
    app_label varchar(100) not null,
    model     varchar(100) not null,
    constraint django_content_type_app_label_model_76bd3d3b_uniq
        unique (app_label, model)
);

create table auth_permission
(
    id              int auto_increment
        primary key,
    name            varchar(255) not null,
    content_type_id int          not null,
    codename        varchar(100) not null,
    constraint auth_permission_content_type_id_codename_01ab375a_uniq
        unique (content_type_id, codename),
    constraint auth_permission_content_type_id_2f476e4b_fk_django_co
        foreign key (content_type_id) references django_content_type (id)
);

create table auth_group_permissions
(
    id            int auto_increment
        primary key,
    group_id      int not null,
    permission_id int not null,
    constraint auth_group_permissions_group_id_permission_id_0cd325b0_uniq
        unique (group_id, permission_id),
    constraint auth_group_permissio_permission_id_84c5c92e_fk_auth_perm
        foreign key (permission_id) references auth_permission (id),
    constraint auth_group_permissions_group_id_b120cbf9_fk_auth_group_id
        foreign key (group_id) references auth_group (id)
);

create table auth_user_user_permissions
(
    id            int auto_increment
        primary key,
    user_id       int not null,
    permission_id int not null,
    constraint auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
        unique (user_id, permission_id),
    constraint auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm
        foreign key (permission_id) references auth_permission (id),
    constraint auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id
        foreign key (user_id) references auth_user (id)
);

create table django_admin_log
(
    id              int auto_increment
        primary key,
    action_time     datetime(6)       not null,
    object_id       longtext          null,
    object_repr     varchar(200)      not null,
    action_flag     smallint unsigned not null,
    change_message  longtext          not null,
    content_type_id int               null,
    user_id         int               not null,
    constraint django_admin_log_content_type_id_c4bce8eb_fk_django_co
        foreign key (content_type_id) references django_content_type (id),
    constraint django_admin_log_user_id_c564eba6_fk_auth_user_id
        foreign key (user_id) references auth_user (id)
);

create table django_migrations
(
    id      int auto_increment
        primary key,
    app     varchar(255) not null,
    name    varchar(255) not null,
    applied datetime(6)  not null
);

create table django_session
(
    session_key  varchar(40) not null
        primary key,
    session_data longtext    not null,
    expire_date  datetime(6) not null
);

create index django_session_expire_date_a5c62663
    on django_session (expire_date);

create table reservarcita_antecedentealergico
(
    id          int auto_increment
        primary key,
    descripcion varchar(300) not null
);

create table reservarcita_antecedentefamiliar
(
    id          int auto_increment
        primary key,
    grado       varchar(19)  not null,
    descripcion varchar(300) not null
);

create table reservarcita_antecedentegeneral
(
    id             int auto_increment
        primary key,
    habitos        varchar(300) not null,
    medicamentos   varchar(300) not null,
    transfunciones varchar(300) not null,
    patologias     varchar(300) not null
);

create table reservarcita_especialidad
(
    codigo_especialidad int         not null
        primary key,
    nombre              varchar(25) not null
);

create table reservarcita_persona
(
    id                 int auto_increment
        primary key,
    nombres            varchar(50)  not null,
    apellidos          varchar(50)  not null,
    sexo               varchar(12)  not null,
    estado_civil       varchar(20)  not null,
    correo_electronico varchar(50)  not null,
    celular            int          not null,
    direccion          varchar(100) not null,
    dni                int          not null,
    fecha_nacimiento   date         not null,
    contrasenia        varchar(35)  not null
);

create table reservarcita_sede
(
    id        int auto_increment
        primary key,
    ubicacion varchar(100) not null
);

create table reservarcita_seguro
(
    id          int auto_increment
        primary key,
    tipo        varchar(25) not null,
    aseguradora varchar(25) not null
);

create table reservarcita_tecnologo
(
    persona_id int         not null
        primary key,
    area       varchar(12) not null,
    constraint ReservarCita_tecnolo_persona_id_7cade8ad_fk_ReservarC
        foreign key (persona_id) references reservarcita_persona (id)
);

create table reservarcita_transaccion
(
    id               int auto_increment
        primary key,
    codigo_operacion int  not null,
    fecha            date not null,
    monto            int  not null
);

create table reservarcita_triaje
(
    id    int auto_increment
        primary key,
    peso  double not null,
    talla double not null
);

create table reservarcita_paciente
(
    persona_id              int        not null
        primary key,
    id_seguro               int        not null,
    tipo_sangre             varchar(3) not null,
    aseguradora_id          int        null,
    antecedente_alergico_id int        null,
    antecedente_familiar_id int        null,
    antecedente_general_id  int        null,
    triaje_id               int        null,
    constraint ReservarCita_pacient_antecedente_alergico_76ad0f49_fk_ReservarC
        foreign key (antecedente_alergico_id) references reservarcita_antecedentealergico (id),
    constraint ReservarCita_pacient_antecedente_familiar_4e04c94a_fk_ReservarC
        foreign key (antecedente_familiar_id) references reservarcita_antecedentefamiliar (id),
    constraint ReservarCita_pacient_antecedente_general__0373239c_fk_ReservarC
        foreign key (antecedente_general_id) references reservarcita_antecedentegeneral (id),
    constraint ReservarCita_pacient_aseguradora_id_82ca174e_fk_ReservarC
        foreign key (aseguradora_id) references reservarcita_seguro (id),
    constraint ReservarCita_pacient_persona_id_dff8d5cc_fk_ReservarC
        foreign key (persona_id) references reservarcita_persona (id),
    constraint ReservarCita_pacient_triaje_id_1d0b8d3c_fk_ReservarC
        foreign key (triaje_id) references reservarcita_triaje (id)
);

create table reservarcita_turno
(
    id_turno    varchar(8) not null
        primary key,
    hora_inicio time(6)    not null,
    hora_fin    time(6)    not null
);

create table reservarcita_horario
(
    id          int auto_increment
        primary key,
    hora_inicio time(6)    not null,
    hora_fin    time(6)    not null,
    turno_id    varchar(8) not null,
    constraint ReservarCita_horario_turno_id_d70ae661_fk_ReservarC
        foreign key (turno_id) references reservarcita_turno (id_turno)
);

create table reservarcita_medico
(
    habilitado      tinyint(1) not null,
    persona_id      int        not null
        primary key,
    especialidad_id int        null,
    horario_id      int        null,
    constraint ReservarCita_medico_especialidad_id_b2fca71d_fk_ReservarC
        foreign key (especialidad_id) references reservarcita_especialidad (codigo_especialidad),
    constraint ReservarCita_medico_horario_id_28c32d7b_fk_ReservarC
        foreign key (horario_id) references reservarcita_horario (id),
    constraint ReservarCita_medico_persona_id_7e5af52a_fk_ReservarC
        foreign key (persona_id) references reservarcita_persona (id)
);

create table reservarcita_cita
(
    id             int auto_increment
        primary key,
    fecha          date       not null,
    hora           time(6)    not null,
    confirmacion   tinyint(1) not null,
    medico_id      int        null,
    paciente_id    int        null,
    tecnologo_id   int        null,
    sede_id        int        null,
    transaccion_id int        null,
    constraint ReservarCita_cita_medico_id_e5036c7f_fk_ReservarC
        foreign key (medico_id) references reservarcita_medico (persona_id),
    constraint ReservarCita_cita_paciente_id_9190d809_fk_ReservarC
        foreign key (paciente_id) references reservarcita_paciente (persona_id),
    constraint ReservarCita_cita_sede_id_1db9cad0_fk_ReservarCita_sede_id
        foreign key (sede_id) references reservarcita_sede (id),
    constraint ReservarCita_cita_tecnologo_id_c571a595_fk_ReservarC
        foreign key (tecnologo_id) references reservarcita_tecnologo (persona_id),
    constraint ReservarCita_cita_transaccion_id_c132ffd9_fk_ReservarC
        foreign key (transaccion_id) references reservarcita_transaccion (id)
);

create table resultados_recurso
(
    id          int auto_increment
        primary key,
    fecha       date         not null,
    descripcion varchar(100) not null,
    ruta        varchar(200) not null
);

create table resultados_imagen
(
    id           int auto_increment
        primary key,
    probabilidad double not null,
    `precision`  double not null,
    recurso_id   int    null,
    constraint Resultados_imagen_recurso_id_87c7509f_fk_Resultados_recurso_id
        foreign key (recurso_id) references resultados_recurso (id)
);

create table resultados_diagnostico
(
    id          int auto_increment
        primary key,
    descripcion varchar(200) not null,
    imagen_id   int          null,
    constraint Resultados_diagnosti_imagen_id_b8c863b7_fk_Resultado
        foreign key (imagen_id) references resultados_imagen (id)
);

create table resultados_resonancia
(
    id           int auto_increment
        primary key,
    recurso_id   int null,
    tecnologo_id int null,
    constraint Resultados_resonanci_recurso_id_67281672_fk_Resultado
        foreign key (recurso_id) references resultados_recurso (id),
    constraint Resultados_resonanci_tecnologo_id_bbbfbadd_fk_ReservarC
        foreign key (tecnologo_id) references reservarcita_tecnologo (persona_id)
);

create table resultados_resultado
(
    id            int auto_increment
        primary key,
    cita_id       int null,
    resonancia_id int null,
    constraint Resultados_resultado_cita_id_50f263a8_fk_ReservarCita_cita_id
        foreign key (cita_id) references reservarcita_cita (id),
    constraint Resultados_resultado_resonancia_id_5ecdfcb5_fk_Resultado
        foreign key (resonancia_id) references resultados_resonancia (id)
);

create table resultados_tratamiento
(
    id             int auto_increment
        primary key,
    descripcion    varchar(200) not null,
    Diagnostico_id int          null,
    constraint Resultados_tratamien_Diagnostico_id_6b64a8c3_fk_Resultado
        foreign key (Diagnostico_id) references resultados_diagnostico (id)
);

