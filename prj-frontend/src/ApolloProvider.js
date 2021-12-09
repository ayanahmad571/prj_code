import React from "react";
import App from "./App";
import ApolloClient from "apollo-client";
import { ApolloProvider } from "@apollo/react-hooks";
import { InMemoryCache } from "apollo-cache-inmemory";
import { setContext } from "apollo-link-context";
import { ChakraProvider } from "@chakra-ui/react";
import { createUploadLink } from "apollo-upload-client";
import customTheme from "./utils/theme";
import LocalizationProvider from '@mui/lab/LocalizationProvider';
import DateFnsAdapter from '@mui/lab/AdapterDateFns';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { purple } from '@mui/material/colors';
import Button from '@mui/material/Button';

const uploadLink = createUploadLink({
  uri: process.env.REACT_APP_BACKEND_URL,
  headers: {
    "keep-alive": "true",
  },
});

const authLink = setContext((_, { headers }) => {
  const token = localStorage.getItem("jwtToken");
  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : "",
    },
  };
});

const client = new ApolloClient({
  link: authLink.concat(uploadLink),
  cache: new InMemoryCache(),
  connectToDevTools: true,
});



const theme = createTheme({
  palette: {
    primary: {
      // Purple and green play nicely together.
      main: purple[500],
    },
    secondary: {
      // This is green.A700 as hex.
      main: '#11cb5f',
    },
  },
});


const appExport = () => {
    return (
      <ApolloProvider client={client}>
          <ThemeProvider theme={theme}>
            <LocalizationProvider dateAdapter={DateFnsAdapter}>
              <App />
            </LocalizationProvider>
          </ThemeProvider>
      </ApolloProvider>
    );
  };
export default appExport;
