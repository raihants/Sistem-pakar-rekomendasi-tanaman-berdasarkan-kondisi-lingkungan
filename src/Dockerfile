FROM php:8.1-apache

# copy semua file dari src ke folder apache
COPY . /var/www/html/

# aktifkan mod_rewrite kalau nanti pakai routing
RUN a2enmod rewrite

EXPOSE 80
