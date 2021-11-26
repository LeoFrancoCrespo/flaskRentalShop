DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS boat_item;
DROP TABLE IF EXISTS rentable_item;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE boat_item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    boat_type TEXT NOT NULL,
    capacity_min INTEGER NOT NULL,
    capacity_max INTEGER NOT NULL,
    cost_per_2_hours INTEGER NOT NULL,
    deposit_per_boat INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    rental_location TEXT NOT NULL
);

INSERT INTO 
    boat_item (boat_type,capacity_min,capacity_max,cost_per_2_hours,deposit_per_boat,quantity,rental_location) 
    VALUES ('Kayak (1 peddle)', 1, 1, 15, 50, 100, "main office");
INSERT INTO 
    boat_item (boat_type,capacity_min,capacity_max,cost_per_2_hours,deposit_per_boat,quantity,rental_location) 
    VALUES ('Canoe (2 peddles)', 1, 2, 20, 50, 75, "main office");
INSERT INTO 
    boat_item (boat_type,capacity_min,capacity_max,cost_per_2_hours,deposit_per_boat,quantity,rental_location) 
    VALUES ('Sailboat `Laser`', 1, 1, 74, 800, 50, "main office");
INSERT INTO 
    boat_item (boat_type,capacity_min,capacity_max,cost_per_2_hours,deposit_per_boat,quantity,rental_location) 
    VALUES ('Sailboat `Valk`', 2, 5, 115, 2500, 35, "main office");

CREATE TABLE rentable_item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    cost_per_2_hours INTEGER NOT NULL,
    deposit_per_item INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    remark TEXT NOT NULL,
    rental_location TEXT NOT NULL
);

INSERT INTO 
    rentable_item (item_name,cost_per_2_hours,deposit_per_item,quantity,remark,rental_location) 
    VALUES ('Life Jacket', 0, 25, 500, "","main office");
INSERT INTO 
    rentable_item (item_name,cost_per_2_hours,deposit_per_item,quantity,remark,rental_location) 
    VALUES ('Waterproof Container', 250, 0, 200, "Capacity of 5 litres", "main office");
INSERT INTO 
    rentable_item (item_name,cost_per_2_hours,deposit_per_item,quantity,remark,rental_location) 
    VALUES ('Cool Box', 250, 0, 50, "Capacity of 25 litres", "main office");
INSERT INTO 
    rentable_item (item_name,cost_per_2_hours,deposit_per_item,quantity,remark,rental_location) 
    VALUES ('Navigation Device', 500, 50, 35, "", "main office");
INSERT INTO 
    rentable_item (item_name,cost_per_2_hours,deposit_per_item,quantity,remark,rental_location) 
    VALUES ('Spare Peddle', 750, 25, 50, "", "main office");
INSERT INTO 
    rentable_item (item_name,cost_per_2_hours,deposit_per_item,quantity,remark,rental_location) 
    VALUES ('Tent', 450, 100, 35, "2 person tents", "main office");
INSERT INTO 
    rentable_item (item_name,cost_per_2_hours,deposit_per_item,quantity,remark,rental_location) 
    VALUES ('Electric Furnace', 215, 0, 20, "", "main office");