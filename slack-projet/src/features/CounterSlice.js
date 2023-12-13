import { CreateSlice } from '@reduxjs/toolkit';

export const counterSlice = CreateSlice({
    name: 'counter',
    initialState: {
        value : 0,
    },
   reducers: {
    increment: state => {
        state.value += 1;
    },
    decrement: state => {
        state.value -= 1
    },
    incrementByAmount: (state,action) => {
        state.value += action.payload;
    },
   }, 
})






