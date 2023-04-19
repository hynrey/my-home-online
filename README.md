# my-home-online

Пользователь для проверки функционала login: **admin** pass: **admin123**

Под каждый вопрос создано свое приложение. Все они задокументированы с помощью инструмента drf-spectacular, доступному по адресу - http://127.0.0.1/api/schema/swagger-ui/

Для проверки вопроса 3 можно загрузить данные в базу данных с помощью 
```
python3 manage.py loaddata ./data.json
```
```
python3 manage.py loaddata ./properties.json
```

Миграция базы данных уже создана, поэтому можно не делать миграции.

1. Передача пользователя при POST запросе
   
    Для того чтобы правильно сохранить пользователя который вносит изменения с помощью POST запроса, необходимо удостовериться, что пользователь авторизован `request.user.is_authenticated` и при создании Entity передать параметр `modified_by` функции `save()` например `serializer.save(modified_by=self.request.user)`. Исходники доступны в файле 📁 `api_solution1/views.py`

    ```python
    def post(self, request, *args, **kwargs):
        # Сеарилизуем получаемые данные
        serializer = EntitySerializer(data=request.data)
        # Проверяем валидность данных сериализатора
        if serializer.is_valid():
            # Проверяем передан ли нам BasicAuth
            if request.user.is_authenticated:
                # Создаем Entity с пользователем обратившимся к API ресурсу
                serializer.save(modified_by=self.request.user)
                return Response({"message": "Entity Created"}, status=status.HTTP_201_CREATED)
            return Response({"message": "Authentication Failed"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"message": "Bad request to API"}, status=status.HTTP_400_BAD_REQUEST)
    ```

2. Кастомная валидация поля `data[value]`
   
   Для того, чтобы валидировать поле `data[value]` как `value` был перегружена функция `is_valid` в сериализаторе, в итоге функция возвращает True при валидации `data[value]` и в том случае если `if isinstance(data_value, int):` это тип данных `integer`. Далее при создании Entity берется значение `data_value = self.initial_data.get(
            "data[value]")` и сохраняется средствами модели.
    Исходники доступны в файле 📁 `api_solution2/serializers.py`

    ```python
    def is_valid(self, *, raise_exception=False):
        if self.initial_data.get("data[value]", None) is not None:
            data_value = self.initial_data.get("data[value]")
            if isinstance(data_value, int):
                return True
            else:
                return False
        return super().is_valid(raise_exception=raise_exception)

    def save(self, modified_by):
        data_value = self.initial_data.get(
            "data[value]")
        e = Entity(value=data_value, modified_by=modified_by)
        e.save()
    ```

3. Кастомное отображение Properties.
   
   Для отображения модели Properties в формате `{"key_name":"value"}` используется поле `DRF SerializerMethodField` с помощью которого создается новый `dict` под каждый объект Entity. Исходники доступны в файле 📁 `api_solution3/serializers.py`

   ```python
   class EntitySerializer(serializers.ModelSerializer):
    value = serializers.IntegerField()
    properties = serializers.SerializerMethodField(read_only=True)

    def get_properties(self, obj):
        properties = {}
        for property in obj.properties.all():
            properties.update({property.key: property.value})
        return properties

    class Meta:
        model = Entity
        fields = "__all__"
   ``` 
