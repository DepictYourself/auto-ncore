/* eslint-disable @typescript-eslint/no-unused-vars */
import {
  Navbar,
  NavbarBrand,
  NavbarCollapse,
  NavbarLink,
  NavbarToggle,
} from "flowbite-react";
import { Link } from "react-router-dom";

const navbar = () => {
  return (
    <Navbar fluid>
      <NavbarBrand href="/">
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Auto-nCore</span>
      </NavbarBrand>
      <div className="flex md:order-2">
        {/* 
        <Dropdown
          arrowIcon={false}
          inline
          label={
            <Avatar alt="User settings" rounded />
          }
        >
          <DropdownHeader>
            <span className="block text-sm">Bonnie Green</span>
            <span className="block truncate text-sm font-medium">name@flowbite.com</span>
          </DropdownHeader>
          <DropdownItem>Dashboard</DropdownItem>
          <DropdownItem>Settings</DropdownItem>
          <DropdownItem>Earnings</DropdownItem>
          <DropdownDivider />
          <DropdownItem>Sign out</DropdownItem>
        </Dropdown> 
        */}
        <NavbarToggle />
      </div>
      <NavbarCollapse>
        <NavbarLink active>
          <Link to="/">Movies</Link>
        </NavbarLink>
        <NavbarLink >
          <Link to="/downloads">Downloads</Link>
        </NavbarLink>
      </NavbarCollapse>
    </Navbar>
  )
}

export default navbar