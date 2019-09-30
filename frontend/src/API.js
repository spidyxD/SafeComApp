const BASE_URL = 'http://localhost:8000';

const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
const randomNumber = (min = 0, max = 1) =>
    Math.floor(Math.random() * (max - min + 1)) + min;
const simulateNetworkLatency = (min = 30, max = 1500) =>
    delay(randomNumber(min, max));

async function callApi(endpoint, options = {}) {
    //await simulateNetworkLatency();

    options.headers = {
        'Content-Type': 'application/json',
        Accept: 'application/json',
        method: 'GET'
    };

    const url = endpoint;
    //BASE_URL + endpoint;
    const response = await fetch(url, options);
    const data = await response.json();

    return data;
}

const api = {
    actions: {
      async listPersons() {
            try {
                return callApi('/api/persons/');
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }              
        },
        listVehicles() {
            try {
                return callApi('/api/vehicles/');
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }              
        },
        listRecords() {
            try {
                return callApi('/api/recordVisits/');
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }              
        },
        listBlackList() {
            try {
                return callApi('/api/blackList/');
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }              
        },
        createPerson(person) {
            try {
                return callApi(`/api/person/create`, {
                    method: 'POST',
                    body: JSON.stringify(person),
                });
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }        
        },
        createVehicle(vehicle) {
            try {
                return callApi(`/api/vehicle/create`, {
                    method: 'POST',
                    body: JSON.stringify(vehicle),
                });
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }        
        },
        createRecord(record) {
            try {
                return callApi(`/api/recordVisit/create`, {
                    method: 'POST',
                    body: JSON.stringify(record),
                });
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }        
        },
        createBlackListRecord(record) {
            try {
                return callApi(`/api/blackList/create`, {
                    method: 'POST',
                    body: JSON.stringify(record),
                });
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }        
        },
        searchVehicle(placa) {
            try {
                return callApi(`/api/vehicle/${placa}`);
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }                 
        },
        searchPerson(id) {
            try {
                return callApi(`/api/person/${id}`);
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }                 
        },
        updateVehicle(placa, updates) {
            try {
                return callApi(`/api/vehicle/${placa}/update`, {
                    method: 'PUT',
                    body: JSON.stringify(updates),
                });
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }  
        },
        updatePeople(id, updates) {
            try {
                return callApi(`/api/person/${id}/update`, {
                    method: 'PUT',
                    body: JSON.stringify(updates),
                });
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }  
        },
        removeVehicle(placa) {
            try {
                return callApi(`/api/vehicle/${placa}/delete`);
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }     
        },
        removePerson(id) {
            try {
                return callApi(`/api/person/${id}/delete`);
            } catch (error) {
                throw new Error('500: Server error. '+ error);
            }     
        }
        ,
    },
};

export default api;