import api from './apiService'
import { Meme } from '../types'
export const postService = {
  async getRandomAmount (amt: number) {
    let result:Meme[] = await api.get(`/images/random?limit=${amt}`)
    return result
  },
  async getMatchingText (term: string) {
    let result = await api.get(`/images/search/${term}`)
    return result
  }
}
