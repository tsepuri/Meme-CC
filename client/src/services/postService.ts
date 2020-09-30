import api from './apiService'
import { Meme } from '../types'
import { compile } from 'json-schema-to-typescript'
export const postService = {
  async getRandomAmount (amt: number) {
    let result = await api.get<Meme[]>(`/images/random?limit=${amt}`)
    let meme = <Meme>result[0]
    return result
  }
}
