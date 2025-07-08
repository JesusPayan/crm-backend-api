-- view: vwshowgroups
create or replace
algorithm = UNDEFINED view `control_escolar_bd`.`vwshowgroups` as
select
    `g`.`id` as `id`,
    `g`.`group_name` as `group_name`,
    `g`.`group_level` as `group_level`,
    `g`.`group_capacity` as `group_capacity`
    `g`.`group_uuid` as `group_uudi`
from
    `control_escolar_bd`.`groups` `g`;


    create or replace
algorithm = UNDEFINED view `control_escolar_bd`.`show_active_students` as
select
    `u`.`id` as `id`,
    `u`.`name` as `name`,
    `u`.`last_name` as `last_name`,
    `u`.`age` as `age`,
    `u`.`email` as `email`,
    `u`.`password` as `password`,
    `u`.`profile_picture` as `profile_picture`,
    `u`.`uu_id` as `uu_id`,
    `u`.`create_date` as `create_date`,
    `u`.`active` as `active`,
    `u`.`last_login` as `last_login`,
    `u`.`id_role` as `id_role`,
    `u`.`group_id` as `group_id`
from
    `control_escolar_bd`.`users` `u`
where
    ((`u`.`id_role` = 2)
        and (`u`.`active` = 1));