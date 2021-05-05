import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.scss";
import { Row, Col, Form, Container, Card } from "react-bootstrap";
import { Link } from "react-router-dom";

export const Contact = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container contactcus">
			<Row>
				<Col>
					<Container>
						<div>
							<h3>Contáctenos</h3>
						</div>
						<Card style={{ width: "40rem" }}>
							<Card.Body>
								<Form.Group>
									<Form.Control type="text" placeholder="Nombre" />
									<br />
									<Form.Control type="text" placeholder="Correo" />
									<br />
									<Form.Control type="text" placeholder="Número de contacto" />
									<br />
									<Form.Control type="text" placeholder="Mensaje" />
								</Form.Group>
							</Card.Body>
						</Card>
					</Container>
				</Col>
				<Col>
					<Container>
						<Card style={{ width: "18rem" }}>
							<Card.Body>
								<Card.Title>Kalendar-FIT</Card.Title>
								<Card.Subtitle className="mb-2 text-muted">Telefono 2299-05-06</Card.Subtitle>
								<Card.Text>
									Estamos ubicados en Desamparados. De la estación de servicio La Primavera, 300m
									Norte y 75m Este. Local esquinero de color blanco con verde.{" "}
								</Card.Text>
								<p>Buscanos en nuestras redes sociales</p>
								<Card.Link href="#">
									<i
										className="fab fa-facebook-square fa-2x d-inline-block align-top"
										width="30"
										height="30"
									/>
								</Card.Link>
								<Card.Link href="#">
									<i
										className="fab fa-instagram fa-2x d-inline-block align-top"
										width="30"
										height="30"
									/>
								</Card.Link>
							</Card.Body>
						</Card>
					</Container>
				</Col>
			</Row>
			<Row />
		</div>
	);
};
