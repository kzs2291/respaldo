import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { Navbar, Nav, Button, Dropdown, DropdownButton, FormControl } from "react-bootstrap";
import { Context } from "../store/appContext";

export const Navbar1 = () => {
	const { store, actions } = useContext(Context);
	const { islogin } = store;
	const { setLogin } = actions;

	return (
		<div className="container navpad">
			<Navbar bg="light" expand="lg">
				<Navbar.Brand href="/">
					<i className="fas fa-dumbbell fa-2x d-inline-block align-top" width="30" height="30" />
				</Navbar.Brand>
				<Navbar.Brand> Kalendar-FIT</Navbar.Brand>
				<Navbar.Toggle aria-controls="basic-navbar-nav" />
				<Navbar.Collapse id="basic-navbar-nav">
					<Nav className="mr-auto">
						<Nav.Link href="/clasesdisponibles">Clases</Nav.Link>
						<Nav.Link href="/contact">Contacto</Nav.Link>
						<Nav.Link href="/crearclase">Contacto</Nav.Link>
					</Nav>

					{islogin ? (
						<Button
							variant="primary buttonspace"
							onClick={() => {
								setLogin(false);
								console.log("login es ", islogin);
							}}>
							Logout
						</Button>
					) : (
						<>
							<Link to="/register">
								<Button variant="primary buttonspace">Registrarme</Button>
							</Link>
							<Link to="/login">
								<Button variant="primary buttonspace">Login</Button>
							</Link>
						</>
					)}
				</Navbar.Collapse>
			</Navbar>
			<script src="https://kit.fontawesome.com/3b05315429.js" crossOrigin="anonymous" />
		</div>
	);
};
