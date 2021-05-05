const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			classRegistration: [],
			classParticipants: []
		},
		actions: {
			// Use getActions to call a function within a fuction
			updateClassRegistration: newClass => {
				const store = getStore();
				store.classRegistration.push(newClass);
			},

			registerToClass: index => {
				const store = getStore();
				const actions = getActions();

				const classRegistration = store.classRegistration.map((elm, i) => {
					if (i === index) elm.cupo = elm.cupo - 1;
					return elm;
				});

				setStore({ classRegistration: classRegistration });

				actions.updateRegisteredClasses(classRegistration, index);
			},

			updateRegisteredClasses: (inArr, idx) => {
				const store = getStore();

				const registeredClass = (({ nombreClase, fechaIni }) => ({ nombreClase, fechaIni }))(inArr[idx]);

				store.classParticipants.push(registeredClass);
			},

			dropFromClass: toRemove => {
				const store = getStore();

				const myUpdatedClasses = store.classParticipants.filter((item, index) => index !== toRemove);

				setStore({ classParticipants: myUpdatedClasses });
			},

			getMessage: () => {
				// fetching data from the backend
				fetch(process.env.BACKEND_URL + "/api/hello")
					.then(resp => resp.json())
					.then(data => setStore({ message: data.message }))
					.catch(error => console.log("Error loading message from backend", error));
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			}
		}
	};
};

export default getState;
