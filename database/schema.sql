CREATE SCHEMA urent;

CREATE TYPE urent.bathroom_type AS ENUM ('BATH', 'SHOWER');

CREATE TABLE urent.description (
    id text NOT NULL,
    bathroom_type urent.bathroom_type,
    towels boolean,
    linen boolean,
    furniture text[],
    barbecue_area boolean,
    garage boolean,
    house_area float,
    room_amount integer,
    floor_amount integer,
    appliances text[],
    utilities text[],

    CONSTRAINT pk_description_id PRIMARY KEY (id)
);

CREATE TABLE urent.house (
    id text NOT NULL,
    description_id text NOT NULL,
    title text NOT NULL,
    price integer NOT NULL,
    max_capacity integer NOT NULL,
    address text NOT NULL,
    availability boolean NOT NULL DEFAULT TRUE,
    photos text[],

    CONSTRAINT pk_house_id PRIMARY KEY (id),
    CONSTRAINT check_price CHECK (price > 0),
    CONSTRAINT check_max_capacity CHECK (max_capacity > 0),
    CONSTRAINT fk_description FOREIGN KEY (description_id)
        REFERENCES urent.description(id)
);

CREATE TYPE urent.communication_method AS ENUM ('PHONE', 'TELEGRAM', 'WHATSAPP');

CREATE TABLE urent.tenant_form (
    id text NOT NULL,
    house_id text NOT NULL,
    name text NOT NULL,
    phone_number text NOT NULL,
    communication_method urent.communication_method DEFAULT 'PHONE':: urent.communication_method,
    guests_number integer NOT NULL,
    check_in date NOT NULL,
    check_out date NOT NULL,
    comment text,

    CONSTRAINT pk_tenant_form_id PRIMARY KEY (id),
    CONSTRAINT fk_house FOREIGN KEY (house_id)
        REFERENCES urent.house(id)
);

CREATE TABLE urent.booking (
    id text NOT NULL,
    tenant_form_id text,
    house_id text NOT NULL,
    check_in date NOT NULL,
    check_out date NOT NULL,

    CONSTRAINT pk_booking_id PRIMARY KEY (id),
    CONSTRAINT fk_house FOREIGN KEY (house_id)
        REFERENCES urent.house(id),
    CONSTRAINT fk_tenant_form FOREIGN KEY (tenant_form_id)
        REFERENCES urent.tenant_form(id)
);

CREATE TABLE urent.owner (
    id text NOT NULL,
    name text NOT NULL,
    phone_number text NOT NULL,
    telegram text,

    CONSTRAINT pk_owner_id PRIMARY KEY (id)
);

CREATE TABLE urent.owner_house (
    house_id text NOT NULL,
    owner_id text NOT NULL,

    CONSTRAINT pk_owner_house PRIMARY KEY (house_id),
    CONSTRAINT fk_house FOREIGN KEY (house_id)
        REFERENCES urent.house,
    CONSTRAINT fk_owner FOREIGN KEY (owner_id)
        REFERENCES urent.owner
)