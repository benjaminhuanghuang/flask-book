## template macro
    ```
    {% macro render_field(field) %}
    <div class="form-group">
        {{ field.label }}
    </div>
    {% endmacro %}
    ```