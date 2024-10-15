create database school;
use school;

create table student(
	id int primary key auto_increment
);

create table prerequisites(
	id int primary key auto_increment
);

create table matriculated(
	id_student int not null,
    id_subject int not null
);

create table _subject(
	id int primary key auto_increment,
    id_teacher int not null
);

create table prerequisites_subject(
	id_subject int not null,
    id_prerequisites int null
);

create table teacher(
	id int primary key auto_increment,
    id_departament int not null
);

create table departament(
	id int primary key auto_increment,
    id_teacher int not null,
    dp_name varchar(45) not null,
    dp_campus varchar(45) not null
);

create table course(
	id int primary key auto_increment,
    id_departament int not null
);

create table course_subject(
	id_subject int not null,
    id_course int not null,
    constraint fk_subject_cs foreign key (id_subject) references _subject (id),
    constraint fk_course_cs foreign key (id_course) references course (id)
);

alter table matriculated add constraint fk_id_student foreign key (id_student) references student (id);
alter table matriculated add constraint fk_id_subject foreign key (id_subject) references _subject (id);
alter table prerequisites_subject add constraint fk_id_subject_ps foreign key (id_subject) references _subject (id);
alter table prerequisites_subject add constraint fk_id_prerequisites foreign key (id_prerequisites) references prerequisites (id);
alter table _subject add constraint fk_id_teacher foreign key (id) references teacher (id);
alter table departament add constraint fk_id_teacher_dp foreign key (id) references teacher (id);
alter table teacher add constraint fk_id_departament foreign key (id) references departament (id);
alter table course add constraint fk_id_departament_c foreign key (id) references departament (id);


