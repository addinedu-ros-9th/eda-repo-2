drop database eda_project;
create database eda_project;
use eda_project;
show tables;

create table eda_project.gu like project_rent.gu;
insert into eda_project.gu select * from project_rent.gu;

create table eda_project.doro like project_rent.doro;
insert into eda_project.doro select * from project_rent.doro;