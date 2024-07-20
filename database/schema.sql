CREATE SCHEMA urent;

create table urent.house (
    id varchar(255) primary key,
    title varchar(255),
    photos varchar(255) /*how??*/,
    price integer,
    max_capacity integer,
    location float[],
    availability boolean,
    calendar varchar /*how??*/
);

create table urent.booking (
    id varchar(255) primary key,
    foreign key (id) references urent.house(id),
    dates date[]
);

create table urent.owner (
    id varchar(255) primary key,
    name varchar(255),
    booking urent.booking[],
    telephone_number text,
    telegram text
);

create table urent.tenant_form (
    id varchar(255) primary key,
    name varchar(255),
    telephone_number text,
    communication_method text,
    guests_number integer,
    dates date[],
    comment text,
    foreign key (id) references house(id)
);

create type urent.bathroom as enum ('bath', 'shower');

create table urent.description (
    id varchar(255) primary key,
    foreign key (id) references urent.house(id),
    bathroom urent.bathroom,
    towels boolean,
    linen boolean,
    furniture varchar[],
    barbecue_area boolean,
    garage boolean,
    house_area float,
    room_amount integer,
    floor_amount integer,
    appliances varchar[],
    utilities varchar[]
);

create table urent.owner_house (
    house_id varchar(255) primary key,
    owner_id varchar(255) 
)