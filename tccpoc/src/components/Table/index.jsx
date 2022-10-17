import React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

export const DataTable = ({ rows }) => {    
    return (
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="caption table">
                <TableHead>
                    <TableRow>
                        <TableCell align="center">Tipo</TableCell>
                        <TableCell align="center">Valor</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {rows?.map(({ type, value }, key) => (
                        <TableRow key={key}>
                            <TableCell align="center">{type}</TableCell>
                            <TableCell align="center">{value}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}
