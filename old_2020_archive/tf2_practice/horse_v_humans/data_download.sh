wget --no-check-certificate https://storage.googleapis.com/laurencemoroney-blog.appspot.com/horse-or-human.zip -O ./horse_v_humans/horse-or-human.zip
mv horse_or_humans.zip data/
cd data
unzip horse_or_humans.zip
rm -rf horse_or_humans.zip

cd ..

wget --no-check-certificate https://storage.googleapis.com/laurencemoroney-blog.appspot.com/validation-horse-or-human.zip -O ./validation_data/horse-or-human.zip
cd validation_data
unzip horse_or_humans.zip
rm -rf horse_or_humans.zip