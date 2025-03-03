# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for six different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` to use its AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.66</td>
    <td align="right">4.44</td>
    <td align="right">3.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">11.08</td>
    <td align="right">11.16</td>
    <td align="right">16.60</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.03</td>
    <td align="right">4.38</td>
    <td align="right">4.37</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.10</td>
    <td align="right">5.74</td>
    <td align="right">5.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">17.03</td>
    <td align="right">15.78</td>
    <td align="right">17.48</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.82</td>
    <td align="right">4.96</td>
    <td align="right">4.94</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.90</td>
    <td align="right">8.87</td>
    <td align="right">8.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.41</td>
    <td align="right">18.46</td>
    <td align="right">16.44</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.38</td>
    <td align="right">5.32</td>
    <td align="right">5.46</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.31</td>
    <td align="right">13.87</td>
    <td align="right">13.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.58</td>
    <td align="right">23.24</td>
    <td align="right">16.75</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.40</td>
    <td align="right">5.92</td>
    <td align="right">5.91</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">11.43</td>
    <td align="right">15.78</td>
    <td align="right">15.80</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">12.12</td>
    <td align="right">9.43</td>
    <td align="right">9.43</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.86</td>
    <td align="right">5.07</td>
    <td align="right">5.07</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.56</td>
    <td align="right">6.73</td>
    <td align="right">6.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.49</td>
    <td align="right">3.18</td>
    <td align="right">3.13</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.47</td>
    <td align="right">5.51</td>
    <td align="right">5.50</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.22</td>
    <td align="right">10.10</td>
    <td align="right">10.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">16.10</td>
    <td align="right">10.72</td>
    <td align="right">9.92</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.29</td>
    <td align="right">6.34</td>
    <td align="right">6.32</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.75</td>
    <td align="right">14.14</td>
    <td align="right">14.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">16.11</td>
    <td align="right">10.71</td>
    <td align="right">9.94</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.75</td>
    <td align="right">6.64</td>
    <td align="right">6.66</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.07</td>
    <td align="right">17.53</td>
    <td align="right">17.51</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.78</td>
    <td align="right">18.26</td>
    <td align="right">7.35</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.06</td>
    <td align="right">13.25</td>
    <td align="right">17.77</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.76</td>
    <td align="right">5.07</td>
    <td align="right">5.07</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.10</td>
    <td align="right">6.05</td>
    <td align="right">6.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">21.08</td>
    <td align="right">19.39</td>
    <td align="right">18.66</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.88</td>
    <td align="right">6.18</td>
    <td align="right">5.25</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.57</td>
    <td align="right">10.41</td>
    <td align="right">10.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">38.24</td>
    <td align="right">34.82</td>
    <td align="right">19.24</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">11.89</td>
    <td align="right">7.97</td>
    <td align="right">9.05</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">13.33</td>
    <td align="right">18.81</td>
    <td align="right">18.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">57.68</td>
    <td align="right">41.46</td>
    <td align="right">24.68</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">16.59</td>
    <td align="right">15.66</td>
    <td align="right">13.02</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">16.74</td>
    <td align="right">18.47</td>
    <td align="right">18.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">12.23</td>
    <td align="right">9.51</td>
    <td align="right">9.51</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.91</td>
    <td align="right">6.04</td>
    <td align="right">6.07</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.62</td>
    <td align="right">8.07</td>
    <td align="right">8.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.97</td>
    <td align="right">3.66</td>
    <td align="right">3.65</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.26</td>
    <td align="right">6.28</td>
    <td align="right">6.30</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.12</td>
    <td align="right">11.83</td>
    <td align="right">12.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">18.68</td>
    <td align="right">14.06</td>
    <td align="right">12.07</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.16</td>
    <td align="right">9.81</td>
    <td align="right">9.98</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">20.11</td>
    <td align="right">18.05</td>
    <td align="right">18.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">21.19</td>
    <td align="right">18.15</td>
    <td align="right">14.21</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">17.80</td>
    <td align="right">13.53</td>
    <td align="right">12.72</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">22.51</td>
    <td align="right">29.60</td>
    <td align="right">27.03</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.18</td>
    <td align="right">4.23</td>
    <td align="right">3.67</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">8.66</td>
    <td align="right">8.21</td>
    <td align="right">14.60</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.17</td>
    <td align="right">3.87</td>
    <td align="right">3.75</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.91</td>
    <td align="right">3.44</td>
    <td align="right">3.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.25</td>
    <td align="right">12.56</td>
    <td align="right">15.90</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.68</td>
    <td align="right">4.36</td>
    <td align="right">4.50</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.54</td>
    <td align="right">3.18</td>
    <td align="right">3.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.35</td>
    <td align="right">15.05</td>
    <td align="right">15.12</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.18</td>
    <td align="right">4.87</td>
    <td align="right">4.88</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.25</td>
    <td align="right">5.90</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.11</td>
    <td align="right">18.69</td>
    <td align="right">15.29</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.83</td>
    <td align="right">5.71</td>
    <td align="right">5.71</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.57</td>
    <td align="right">6.55</td>
    <td align="right">6.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">10.50</td>
    <td align="right">9.10</td>
    <td align="right">9.07</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.82</td>
    <td align="right">4.49</td>
    <td align="right">4.40</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.03</td>
    <td align="right">3.33</td>
    <td align="right">3.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.03</td>
    <td align="right">2.13</td>
    <td align="right">2.13</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.34</td>
    <td align="right">5.10</td>
    <td align="right">5.08</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.48</td>
    <td align="right">3.51</td>
    <td align="right">3.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">10.49</td>
    <td align="right">10.01</td>
    <td align="right">3.41</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.87</td>
    <td align="right">5.88</td>
    <td align="right">5.89</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.52</td>
    <td align="right">5.61</td>
    <td align="right">5.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">4.41</td>
    <td align="right">4.30</td>
    <td align="right">3.37</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.75</td>
    <td align="right">3.06</td>
    <td align="right">3.04</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.05</td>
    <td align="right">6.63</td>
    <td align="right">6.58</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">33.44</td>
    <td align="right">16.74</td>
    <td align="right">7.17</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.02</td>
    <td align="right">10.63</td>
    <td align="right">16.35</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.95</td>
    <td align="right">4.75</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.70</td>
    <td align="right">4.39</td>
    <td align="right">4.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">17.03</td>
    <td align="right">17.14</td>
    <td align="right">17.48</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.92</td>
    <td align="right">5.66</td>
    <td align="right">6.56</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.63</td>
    <td align="right">4.21</td>
    <td align="right">4.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">29.81</td>
    <td align="right">32.93</td>
    <td align="right">18.97</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">8.39</td>
    <td align="right">10.15</td>
    <td align="right">8.78</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">8.39</td>
    <td align="right">8.83</td>
    <td align="right">9.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">58.57</td>
    <td align="right">61.23</td>
    <td align="right">22.88</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">13.07</td>
    <td align="right">14.75</td>
    <td align="right">14.73</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">12.31</td>
    <td align="right">14.41</td>
    <td align="right">13.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">10.66</td>
    <td align="right">9.22</td>
    <td align="right">9.21</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.60</td>
    <td align="right">5.41</td>
    <td align="right">5.31</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.82</td>
    <td align="right">4.27</td>
    <td align="right">4.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.78</td>
    <td align="right">3.08</td>
    <td align="right">3.22</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.65</td>
    <td align="right">6.16</td>
    <td align="right">6.14</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.40</td>
    <td align="right">4.56</td>
    <td align="right">4.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">13.50</td>
    <td align="right">13.17</td>
    <td align="right">6.27</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.55</td>
    <td align="right">10.14</td>
    <td align="right">9.85</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.85</td>
    <td align="right">8.62</td>
    <td align="right">8.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">12.32</td>
    <td align="right">13.74</td>
    <td align="right">10.79</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.56</td>
    <td align="right">9.34</td>
    <td align="right">9.02</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">12.15</td>
    <td align="right">14.59</td>
    <td align="right">15.21</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">21.38</td>
    <td align="right">4.63</td>
    <td align="right">4.68</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">7.52</td>
    <td align="right">5.46</td>
    <td align="right">12.52</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.50</td>
    <td align="right">1.26</td>
    <td align="right">1.26</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.39</td>
    <td align="right">1.78</td>
    <td align="right">1.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.83</td>
    <td align="right">7.86</td>
    <td align="right">12.70</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.44</td>
    <td align="right">1.69</td>
    <td align="right">1.79</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.29</td>
    <td align="right">2.27</td>
    <td align="right">2.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.76</td>
    <td align="right">10.45</td>
    <td align="right">12.13</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.71</td>
    <td align="right">1.73</td>
    <td align="right">1.84</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.53</td>
    <td align="right">3.17</td>
    <td align="right">3.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.01</td>
    <td align="right">12.39</td>
    <td align="right">12.52</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.05</td>
    <td align="right">2.09</td>
    <td align="right">1.98</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">4.97</td>
    <td align="right">4.14</td>
    <td align="right">4.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.07</td>
    <td align="right">1.92</td>
    <td align="right">1.95</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.73</td>
    <td align="right">1.48</td>
    <td align="right">1.49</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.43</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.66</td>
    <td align="right">1.56</td>
    <td align="right">1.49</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.85</td>
    <td align="right">1.56</td>
    <td align="right">1.52</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.90</td>
    <td align="right">3.31</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.16</td>
    <td align="right">3.10</td>
    <td align="right">2.36</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.80</td>
    <td align="right">2.01</td>
    <td align="right">1.78</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.42</td>
    <td align="right">3.23</td>
    <td align="right">3.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">3.12</td>
    <td align="right">3.43</td>
    <td align="right">2.11</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.81</td>
    <td align="right">1.73</td>
    <td align="right">1.76</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.09</td>
    <td align="right">4.24</td>
    <td align="right">4.09</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.57</td>
    <td align="right">14.24</td>
    <td align="right">9.92</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">10.91</td>
    <td align="right">10.53</td>
    <td align="right">19.95</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.06</td>
    <td align="right">3.86</td>
    <td align="right">4.93</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.04</td>
    <td align="right">6.11</td>
    <td align="right">6.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">29.30</td>
    <td align="right">27.32</td>
    <td align="right">25.55</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.85</td>
    <td align="right">6.64</td>
    <td align="right">6.89</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.47</td>
    <td align="right">6.27</td>
    <td align="right">7.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">50.38</td>
    <td align="right">41.52</td>
    <td align="right">26.79</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">11.06</td>
    <td align="right">9.25</td>
    <td align="right">9.77</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">18.46</td>
    <td align="right">16.63</td>
    <td align="right">17.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">80.33</td>
    <td align="right">62.77</td>
    <td align="right">29.15</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.09</td>
    <td align="right">10.70</td>
    <td align="right">9.93</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">23.16</td>
    <td align="right">21.57</td>
    <td align="right">20.62</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.19</td>
    <td align="right">5.13</td>
    <td align="right">5.88</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.21</td>
    <td align="right">3.64</td>
    <td align="right">3.85</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.22</td>
    <td align="right">6.75</td>
    <td align="right">8.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.63</td>
    <td align="right">7.46</td>
    <td align="right">6.55</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">7.79</td>
    <td align="right">6.22</td>
    <td align="right">6.95</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.98</td>
    <td align="right">11.51</td>
    <td align="right">9.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">12.79</td>
    <td align="right">15.68</td>
    <td align="right">13.73</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">15.71</td>
    <td align="right">10.29</td>
    <td align="right">11.05</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">22.25</td>
    <td align="right">17.77</td>
    <td align="right">21.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">18.39</td>
    <td align="right">21.87</td>
    <td align="right">14.71</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">15.27</td>
    <td align="right">12.37</td>
    <td align="right">12.48</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">21.22</td>
    <td align="right">19.43</td>
    <td align="right">22.05</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">34.67</td>
    <td align="right">5.75</td>
    <td align="right">3.83</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.15</td>
    <td align="right">12.53</td>
    <td align="right">17.14</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.83</td>
    <td align="right">4.24</td>
    <td align="right">4.23</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.85</td>
    <td align="right">5.58</td>
    <td align="right">5.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.38</td>
    <td align="right">17.91</td>
    <td align="right">17.74</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.94</td>
    <td align="right">4.86</td>
    <td align="right">4.82</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.68</td>
    <td align="right">8.51</td>
    <td align="right">8.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.63</td>
    <td align="right">21.42</td>
    <td align="right">17.19</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.64</td>
    <td align="right">5.34</td>
    <td align="right">5.34</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.58</td>
    <td align="right">10.85</td>
    <td align="right">11.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.13</td>
    <td align="right">27.45</td>
    <td align="right">17.12</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.99</td>
    <td align="right">5.97</td>
    <td align="right">6.00</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">19.51</td>
    <td align="right">14.63</td>
    <td align="right">14.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">8.90</td>
    <td align="right">10.01</td>
    <td align="right">10.03</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">7.00</td>
    <td align="right">5.24</td>
    <td align="right">5.29</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.26</td>
    <td align="right">5.60</td>
    <td align="right">5.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.91</td>
    <td align="right">4.96</td>
    <td align="right">4.15</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.12</td>
    <td align="right">5.90</td>
    <td align="right">5.94</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.28</td>
    <td align="right">8.78</td>
    <td align="right">8.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">8.41</td>
    <td align="right">10.08</td>
    <td align="right">5.50</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.36</td>
    <td align="right">6.59</td>
    <td align="right">6.60</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.10</td>
    <td align="right">10.51</td>
    <td align="right">10.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">9.29</td>
    <td align="right">9.77</td>
    <td align="right">5.68</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.41</td>
    <td align="right">7.53</td>
    <td align="right">7.54</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.85</td>
    <td align="right">12.59</td>
    <td align="right">13.47</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">40.00</td>
    <td align="right">20.59</td>
    <td align="right">7.26</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.49</td>
    <td align="right">13.16</td>
    <td align="right">17.87</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.05</td>
    <td align="right">4.55</td>
    <td align="right">4.51</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.82</td>
    <td align="right">6.29</td>
    <td align="right">6.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">21.98</td>
    <td align="right">18.80</td>
    <td align="right">18.52</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.53</td>
    <td align="right">5.10</td>
    <td align="right">5.04</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.89</td>
    <td align="right">9.90</td>
    <td align="right">10.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">34.96</td>
    <td align="right">30.29</td>
    <td align="right">21.20</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.08</td>
    <td align="right">6.91</td>
    <td align="right">6.44</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">17.56</td>
    <td align="right">13.24</td>
    <td align="right">13.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">61.50</td>
    <td align="right">71.46</td>
    <td align="right">23.93</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">13.87</td>
    <td align="right">8.34</td>
    <td align="right">8.26</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">25.93</td>
    <td align="right">20.18</td>
    <td align="right">20.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">9.02</td>
    <td align="right">10.11</td>
    <td align="right">10.08</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.96</td>
    <td align="right">5.55</td>
    <td align="right">5.57</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.39</td>
    <td align="right">6.32</td>
    <td align="right">6.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.21</td>
    <td align="right">5.34</td>
    <td align="right">4.43</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.30</td>
    <td align="right">6.43</td>
    <td align="right">6.38</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">19.14</td>
    <td align="right">9.31</td>
    <td align="right">9.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.94</td>
    <td align="right">10.82</td>
    <td align="right">6.27</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">11.22</td>
    <td align="right">7.21</td>
    <td align="right">7.17</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">18.36</td>
    <td align="right">13.00</td>
    <td align="right">13.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">12.47</td>
    <td align="right">14.52</td>
    <td align="right">9.66</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">14.50</td>
    <td align="right">12.85</td>
    <td align="right">11.78</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">26.25</td>
    <td align="right">18.10</td>
    <td align="right">18.82</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">63.84</td>
    <td align="right">91.97</td>
    <td align="right">16.98</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.93</td>
    <td align="right">42.25</td>
    <td align="right">36.69</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.45</td>
    <td align="right">15.93</td>
    <td align="right">16.01</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.46</td>
    <td align="right">20.67</td>
    <td align="right">20.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.56</td>
    <td align="right">64.31</td>
    <td align="right">40.94</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.49</td>
    <td align="right">19.51</td>
    <td align="right">19.45</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.52</td>
    <td align="right">27.64</td>
    <td align="right">26.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">45.43</td>
    <td align="right">78.70</td>
    <td align="right">38.38</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.63</td>
    <td align="right">18.73</td>
    <td align="right">18.72</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.57</td>
    <td align="right">33.54</td>
    <td align="right">34.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">57.31</td>
    <td align="right">98.40</td>
    <td align="right">38.08</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.46</td>
    <td align="right">18.98</td>
    <td align="right">18.98</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">36.24</td>
    <td align="right">38.70</td>
    <td align="right">38.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.55</td>
    <td align="right">13.73</td>
    <td align="right">13.84</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.20</td>
    <td align="right">19.79</td>
    <td align="right">19.76</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.77</td>
    <td align="right">22.27</td>
    <td align="right">22.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.98</td>
    <td align="right">16.66</td>
    <td align="right">16.10</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.17</td>
    <td align="right">18.92</td>
    <td align="right">18.83</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.78</td>
    <td align="right">29.24</td>
    <td align="right">29.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.85</td>
    <td align="right">20.12</td>
    <td align="right">19.77</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.47</td>
    <td align="right">18.89</td>
    <td align="right">18.50</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.63</td>
    <td align="right">46.61</td>
    <td align="right">46.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">24.71</td>
    <td align="right">26.01</td>
    <td align="right">26.06</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.08</td>
    <td align="right">20.33</td>
    <td align="right">20.29</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">79.49</td>
    <td align="right">56.20</td>
    <td align="right">56.85</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">103.25</td>
    <td align="right">130.52</td>
    <td align="right">33.86</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">34.60</td>
    <td align="right">61.01</td>
    <td align="right">61.27</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">17.15</td>
    <td align="right">18.45</td>
    <td align="right">24.86</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">30.46</td>
    <td align="right">26.03</td>
    <td align="right">24.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">40.34</td>
    <td align="right">82.14</td>
    <td align="right">50.75</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">23.87</td>
    <td align="right">24.31</td>
    <td align="right">24.27</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">26.28</td>
    <td align="right">28.12</td>
    <td align="right">30.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">77.74</td>
    <td align="right">108.96</td>
    <td align="right">53.78</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">24.50</td>
    <td align="right">22.74</td>
    <td align="right">23.99</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">54.76</td>
    <td align="right">51.84</td>
    <td align="right">51.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">93.95</td>
    <td align="right">149.53</td>
    <td align="right">54.05</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">43.13</td>
    <td align="right">34.82</td>
    <td align="right">27.23</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">49.55</td>
    <td align="right">63.81</td>
    <td align="right">61.25</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">10.95</td>
    <td align="right">14.55</td>
    <td align="right">14.13</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">17.18</td>
    <td align="right">21.02</td>
    <td align="right">21.76</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">38.25</td>
    <td align="right">25.74</td>
    <td align="right">25.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">15.38</td>
    <td align="right">19.82</td>
    <td align="right">19.99</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">17.82</td>
    <td align="right">23.58</td>
    <td align="right">24.49</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">56.63</td>
    <td align="right">33.64</td>
    <td align="right">32.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">15.94</td>
    <td align="right">23.54</td>
    <td align="right">29.01</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">22.71</td>
    <td align="right">23.94</td>
    <td align="right">21.95</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">68.91</td>
    <td align="right">56.65</td>
    <td align="right">61.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">41.16</td>
    <td align="right">70.49</td>
    <td align="right">75.89</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">49.00</td>
    <td align="right">41.86</td>
    <td align="right">47.11</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">146.24</td>
    <td align="right">115.21</td>
    <td align="right">108.01</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">58.95</td>
    <td align="right">10.41</td>
    <td align="right">7.01</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">13.22</td>
    <td align="right">21.55</td>
    <td align="right">26.47</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.68</td>
    <td align="right">11.79</td>
    <td align="right">11.55</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.04</td>
    <td align="right">15.61</td>
    <td align="right">15.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">18.41</td>
    <td align="right">34.00</td>
    <td align="right">28.95</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">11.22</td>
    <td align="right">13.14</td>
    <td align="right">13.43</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">16.14</td>
    <td align="right">20.82</td>
    <td align="right">21.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">23.19</td>
    <td align="right">44.49</td>
    <td align="right">28.06</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">12.73</td>
    <td align="right">14.62</td>
    <td align="right">14.30</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">22.45</td>
    <td align="right">29.67</td>
    <td align="right">30.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">32.17</td>
    <td align="right">58.25</td>
    <td align="right">29.21</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.38</td>
    <td align="right">15.19</td>
    <td align="right">15.10</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">29.95</td>
    <td align="right">36.58</td>
    <td align="right">35.87</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">6.48</td>
    <td align="right">8.65</td>
    <td align="right">8.74</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.06</td>
    <td align="right">13.62</td>
    <td align="right">13.33</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">12.88</td>
    <td align="right">16.14</td>
    <td align="right">15.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.36</td>
    <td align="right">12.97</td>
    <td align="right">13.08</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.37</td>
    <td align="right">15.31</td>
    <td align="right">15.30</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.12</td>
    <td align="right">21.38</td>
    <td align="right">21.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">12.77</td>
    <td align="right">17.14</td>
    <td align="right">16.32</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">13.65</td>
    <td align="right">15.64</td>
    <td align="right">15.76</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">24.74</td>
    <td align="right">28.50</td>
    <td align="right">30.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">16.26</td>
    <td align="right">20.47</td>
    <td align="right">20.37</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">14.81</td>
    <td align="right">16.98</td>
    <td align="right">17.27</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">30.64</td>
    <td align="right">34.95</td>
    <td align="right">34.66</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">71.04</td>
    <td align="right">42.19</td>
    <td align="right">9.96</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">13.55</td>
    <td align="right">21.42</td>
    <td align="right">27.13</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.37</td>
    <td align="right">11.96</td>
    <td align="right">12.42</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.51</td>
    <td align="right">16.60</td>
    <td align="right">16.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">18.25</td>
    <td align="right">33.28</td>
    <td align="right">28.54</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">11.40</td>
    <td align="right">12.97</td>
    <td align="right">13.13</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">15.97</td>
    <td align="right">20.49</td>
    <td align="right">20.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.04</td>
    <td align="right">44.88</td>
    <td align="right">29.26</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">12.94</td>
    <td align="right">14.12</td>
    <td align="right">13.93</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">22.62</td>
    <td align="right">30.38</td>
    <td align="right">30.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">29.74</td>
    <td align="right">57.02</td>
    <td align="right">28.18</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">13.34</td>
    <td align="right">14.99</td>
    <td align="right">15.21</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">28.07</td>
    <td align="right">34.91</td>
    <td align="right">34.89</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">6.89</td>
    <td align="right">9.04</td>
    <td align="right">8.80</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">11.39</td>
    <td align="right">13.56</td>
    <td align="right">13.59</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.12</td>
    <td align="right">17.16</td>
    <td align="right">17.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">10.64</td>
    <td align="right">12.83</td>
    <td align="right">12.88</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">12.76</td>
    <td align="right">14.16</td>
    <td align="right">14.67</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">16.71</td>
    <td align="right">20.51</td>
    <td align="right">20.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">12.13</td>
    <td align="right">15.52</td>
    <td align="right">16.14</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">13.99</td>
    <td align="right">15.62</td>
    <td align="right">15.91</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">24.28</td>
    <td align="right">30.10</td>
    <td align="right">29.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">15.96</td>
    <td align="right">20.90</td>
    <td align="right">21.08</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">15.10</td>
    <td align="right">16.76</td>
    <td align="right">16.66</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">31.54</td>
    <td align="right">34.51</td>
    <td align="right">34.37</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">42.60</td>
    <td align="right">8.67</td>
    <td align="right">6.66</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">55.00</td>
    <td align="right">53.39</td>
    <td align="right">36.80</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.02</td>
    <td align="right">17.17</td>
    <td align="right">20.47</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.93</td>
    <td align="right">41.67</td>
    <td align="right">41.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">84.24</td>
    <td align="right">77.63</td>
    <td align="right">38.23</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">20.28</td>
    <td align="right">18.64</td>
    <td align="right">20.74</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">24.54</td>
    <td align="right">56.68</td>
    <td align="right">57.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">104.24</td>
    <td align="right">96.52</td>
    <td align="right">37.27</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">21.51</td>
    <td align="right">19.11</td>
    <td align="right">20.53</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">36.04</td>
    <td align="right">77.00</td>
    <td align="right">77.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">133.84</td>
    <td align="right">120.32</td>
    <td align="right">37.91</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">23.76</td>
    <td align="right">20.23</td>
    <td align="right">21.16</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">41.65</td>
    <td align="right">91.33</td>
    <td align="right">91.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.94</td>
    <td align="right">28.83</td>
    <td align="right">28.85</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">21.63</td>
    <td align="right">22.10</td>
    <td align="right">24.84</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">22.92</td>
    <td align="right">40.10</td>
    <td align="right">41.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">16.04</td>
    <td align="right">32.45</td>
    <td align="right">23.72</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">23.52</td>
    <td align="right">23.83</td>
    <td align="right">25.06</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">28.91</td>
    <td align="right">56.45</td>
    <td align="right">58.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">26.49</td>
    <td align="right">52.57</td>
    <td align="right">36.84</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">25.69</td>
    <td align="right">26.49</td>
    <td align="right">27.22</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">41.72</td>
    <td align="right">78.09</td>
    <td align="right">78.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0262</td>
    <td align="right">25.93</td>
    <td align="right">51.04</td>
    <td align="right">37.84</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">27.19</td>
    <td align="right">28.64</td>
    <td align="right">28.58</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">47.64</td>
    <td align="right">91.85</td>
    <td align="right">92.23</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">68.86</td>
    <td align="right">37.10</td>
    <td align="right">12.68</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">63.12</td>
    <td align="right">57.68</td>
    <td align="right">41.59</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">20.27</td>
    <td align="right">18.02</td>
    <td align="right">22.84</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">22.29</td>
    <td align="right">43.93</td>
    <td align="right">42.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">99.08</td>
    <td align="right">102.81</td>
    <td align="right">44.78</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">24.67</td>
    <td align="right">20.50</td>
    <td align="right">26.59</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">37.19</td>
    <td align="right">67.32</td>
    <td align="right">76.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">181.18</td>
    <td align="right">147.22</td>
    <td align="right">46.64</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">33.54</td>
    <td align="right">37.53</td>
    <td align="right">37.99</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">51.64</td>
    <td align="right">89.54</td>
    <td align="right">86.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">251.78</td>
    <td align="right">252.23</td>
    <td align="right">61.09</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">57.26</td>
    <td align="right">39.15</td>
    <td align="right">40.04</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">58.42</td>
    <td align="right">109.49</td>
    <td align="right">108.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">23.53</td>
    <td align="right">44.85</td>
    <td align="right">51.51</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">30.38</td>
    <td align="right">33.49</td>
    <td align="right">33.44</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">29.96</td>
    <td align="right">44.58</td>
    <td align="right">55.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">21.27</td>
    <td align="right">61.75</td>
    <td align="right">51.92</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">39.88</td>
    <td align="right">40.48</td>
    <td align="right">43.92</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">66.34</td>
    <td align="right">102.42</td>
    <td align="right">98.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">61.73</td>
    <td align="right">124.13</td>
    <td align="right">103.88</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">75.35</td>
    <td align="right">78.81</td>
    <td align="right">75.08</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">71.61</td>
    <td align="right">105.85</td>
    <td align="right">106.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">66.13</td>
    <td align="right">126.97</td>
    <td align="right">116.94</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">85.46</td>
    <td align="right">87.29</td>
    <td align="right">89.63</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">96.88</td>
    <td align="right">137.82</td>
    <td align="right">139.57</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
