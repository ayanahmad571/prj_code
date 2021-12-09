import { Container, Typography, Stack, Divider, Button } from "@mui/material";
import { Doughnut } from "react-chartjs-2";
import LineChart from "../components/Charts/LineChart/LineChart";

import StaticDatePicker from "../components/DatePicker/DatePicker";

const labels = ["A", "B", "C", "AA", "BV", "CSD", "Df"];
const data = {
  labels: labels,
  datasets: [
    {
      label: "My First Dataset",
      data: [65, 59, 80, 81, 56, 55, 40],
      fill: false,
      borderColor: "rgb(75, 192, 192)",
      tension: 0.1,
    },
  ],
};

const HomePage = () => {
  return (
    <Container mt="10">
      <Stack>
        <Typography variant="h3" component="div" gutterBottom>
          PRESIDENTIAL ELECTION BOT DETECTOR
        </Typography>
        <br />
        <Divider />
        <Typography variant="h4">User Input</Typography>
        <StaticDatePicker />
        <Button variant="contained" color="success">
          Success
        </Button>
        <br />
        <br />
        <br />

        <Divider />
        <Typography variant="h4">Server Response</Typography>

        <LineChart />
      </Stack>
    </Container>
  );
};

export default HomePage;
