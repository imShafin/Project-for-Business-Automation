document.addEventListener('DOMContentLoaded', function () {
    var dataTable = new DataTable('#carTable');
    document.getElementById('carForm').addEventListener('submit', function (e) {
        e.preventDefault();

        var name = document.getElementById('name').value;
        var model = document.getElementById('model').value;
        var year = document.getElementById('year').value;
        var carType = document.getElementById('carType').value;

        var additionalFields = '';
        if (carType === 'GasCar') {
            additionalFields = document.getElementById('additionalFields').value + ' MPG';
        } else if (carType === 'ElectricCar') {
            additionalFields = document.getElementById('additionalFields').value + ' kWh';
        }
        dataTable.row.add([name, model, year, carType, additionalFields]).draw(false);
        document.getElementById('carForm').reset();
    });

    document.getElementById('carType').addEventListener('change', function () {
        var carType = this.value;
        var additionalFieldsDiv = document.getElementById('additionalFields');

        if (carType === 'GasCar') {
            additionalFieldsDiv.innerHTML = '<label for="gasCapacity">Gas Capacity:</label>' +
                '<input type="text" class="form-control" id="gasCapacity" required>';
        } else if (carType === 'ElectricCar') {
            additionalFieldsDiv.innerHTML = '<label for="electricCapacity">Electric Capacity:</label>' +
                '<input type="text" class="form-control" id="electricCapacity" required>';
        } else {
            additionalFieldsDiv.innerHTML = '';
        }
    });
});

function DataTable(selector) {
    var table = document.querySelector(selector);
    var tbody = table.querySelector('tbody');
    var rows = [];
    this.row = {
        add: function (rowData) {
            var row = document.createElement('tr');
            rowData.forEach(function (data) {
                var cell = document.createElement('td');
                cell.innerHTML = data;
                row.appendChild(cell);
            });
            rows.push(row);
            tbody.appendChild(row);
        }
    };
}
