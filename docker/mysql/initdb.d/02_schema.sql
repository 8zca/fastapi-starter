CREATE TABLE todos (
    id int NOT NULL AUTO_INCREMENT,
    todo varchar(255) NOT NULL,
    status varchar(12),
    created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
