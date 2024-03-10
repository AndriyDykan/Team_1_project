<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

// Перевірка, чи файл вже існує
if (file_exists($target_file)) {
  echo "Вибачте, файл вже існує.";
  $uploadOk = 0;
}

// Перевірка розміру файлу
if ($_FILES["fileToUpload"]["size"] > 500000) {
  echo "Вибачте, ваш файл занадто великий.";
  $uploadOk = 0;
}

// Дозволені розширення файлів
$allowed_extensions = array("jpg", "jpeg", "png", "gif");
if(!in_array($imageFileType, $allowed_extensions)) {
  echo "Вибачте, тільки файли з розширенням JPG, JPEG, PNG & GIF дозволені.";
  $uploadOk = 0;
}

// Перевірка на $uploadOk
if ($uploadOk == 0) {
  echo "Вибачте, ваш файл не завантажено.";
} else {
  if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
    echo "Файл ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " успішно завантажено.";
  } else {
    echo "Виникла помилка під час завантаження файлу.";
  }
}
?>
