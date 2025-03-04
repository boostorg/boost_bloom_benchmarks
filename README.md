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
    <td align="right">25.89</td>
    <td align="right">4.37</td>
    <td align="right">3.47</td>
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
    <td align="right">11.10</td>
    <td align="right">10.67</td>
    <td align="right">16.59</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.03</td>
    <td align="right">4.36</td>
    <td align="right">4.36</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.09</td>
    <td align="right">5.73</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.78</td>
    <td align="right">15.59</td>
    <td align="right">17.43</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.82</td>
    <td align="right">4.92</td>
    <td align="right">4.93</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.92</td>
    <td align="right">8.85</td>
    <td align="right">8.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.46</td>
    <td align="right">18.56</td>
    <td align="right">16.38</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.37</td>
    <td align="right">5.31</td>
    <td align="right">5.44</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.16</td>
    <td align="right">13.69</td>
    <td align="right">13.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">27.22</td>
    <td align="right">22.57</td>
    <td align="right">16.74</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.38</td>
    <td align="right">5.91</td>
    <td align="right">5.90</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">11.27</td>
    <td align="right">15.53</td>
    <td align="right">15.53</td>
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
    <td align="right">12.07</td>
    <td align="right">9.43</td>
    <td align="right">9.43</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.85</td>
    <td align="right">5.13</td>
    <td align="right">5.07</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.51</td>
    <td align="right">6.69</td>
    <td align="right">6.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.47</td>
    <td align="right">3.11</td>
    <td align="right">3.12</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.45</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.16</td>
    <td align="right">10.06</td>
    <td align="right">10.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">16.41</td>
    <td align="right">10.72</td>
    <td align="right">9.89</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.36</td>
    <td align="right">6.36</td>
    <td align="right">6.35</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.78</td>
    <td align="right">14.08</td>
    <td align="right">14.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">16.37</td>
    <td align="right">10.66</td>
    <td align="right">9.92</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.73</td>
    <td align="right">6.60</td>
    <td align="right">6.60</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.04</td>
    <td align="right">17.49</td>
    <td align="right">17.39</td>
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
    <td align="right">30.82</td>
    <td align="right">18.34</td>
    <td align="right">6.59</td>
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
    <td align="right">13.81</td>
    <td align="right">12.78</td>
    <td align="right">17.54</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.63</td>
    <td align="right">4.93</td>
    <td align="right">4.93</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.10</td>
    <td align="right">6.89</td>
    <td align="right">6.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.22</td>
    <td align="right">18.26</td>
    <td align="right">17.87</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.46</td>
    <td align="right">5.56</td>
    <td align="right">5.64</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.16</td>
    <td align="right">10.22</td>
    <td align="right">10.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">26.39</td>
    <td align="right">23.87</td>
    <td align="right">17.54</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.57</td>
    <td align="right">6.52</td>
    <td align="right">6.36</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.25</td>
    <td align="right">15.26</td>
    <td align="right">15.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">34.63</td>
    <td align="right">34.68</td>
    <td align="right">18.13</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">15.05</td>
    <td align="right">16.34</td>
    <td align="right">14.76</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">24.58</td>
    <td align="right">20.48</td>
    <td align="right">25.82</td>
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
    <td align="right">12.22</td>
    <td align="right">9.48</td>
    <td align="right">9.48</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.87</td>
    <td align="right">6.09</td>
    <td align="right">6.08</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.22</td>
    <td align="right">7.60</td>
    <td align="right">7.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.04</td>
    <td align="right">3.79</td>
    <td align="right">3.77</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.97</td>
    <td align="right">6.17</td>
    <td align="right">6.38</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">10.40</td>
    <td align="right">11.20</td>
    <td align="right">11.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">20.09</td>
    <td align="right">12.92</td>
    <td align="right">10.98</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.18</td>
    <td align="right">10.03</td>
    <td align="right">9.82</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">24.74</td>
    <td align="right">21.89</td>
    <td align="right">19.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">22.60</td>
    <td align="right">21.12</td>
    <td align="right">15.20</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">19.21</td>
    <td align="right">17.90</td>
    <td align="right">17.40</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">28.31</td>
    <td align="right">34.96</td>
    <td align="right">33.33</td>
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
    <td align="right">26.34</td>
    <td align="right">4.15</td>
    <td align="right">3.60</td>
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
    <td align="right">9.10</td>
    <td align="right">8.74</td>
    <td align="right">15.26</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.33</td>
    <td align="right">4.06</td>
    <td align="right">3.97</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.07</td>
    <td align="right">3.62</td>
    <td align="right">3.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.79</td>
    <td align="right">13.37</td>
    <td align="right">16.52</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.85</td>
    <td align="right">4.58</td>
    <td align="right">4.72</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.71</td>
    <td align="right">3.38</td>
    <td align="right">3.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.14</td>
    <td align="right">16.68</td>
    <td align="right">15.13</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.36</td>
    <td align="right">5.10</td>
    <td align="right">5.10</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.63</td>
    <td align="right">6.45</td>
    <td align="right">6.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.30</td>
    <td align="right">20.58</td>
    <td align="right">16.09</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.82</td>
    <td align="right">5.88</td>
    <td align="right">5.87</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.88</td>
    <td align="right">6.95</td>
    <td align="right">7.03</td>
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
    <td align="right">10.51</td>
    <td align="right">9.10</td>
    <td align="right">9.10</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.89</td>
    <td align="right">4.71</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.23</td>
    <td align="right">3.58</td>
    <td align="right">3.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.15</td>
    <td align="right">2.26</td>
    <td align="right">2.27</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.49</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.74</td>
    <td align="right">3.74</td>
    <td align="right">3.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">10.84</td>
    <td align="right">9.98</td>
    <td align="right">3.58</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.93</td>
    <td align="right">5.98</td>
    <td align="right">5.99</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.94</td>
    <td align="right">6.16</td>
    <td align="right">6.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">4.70</td>
    <td align="right">4.61</td>
    <td align="right">3.64</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.97</td>
    <td align="right">3.30</td>
    <td align="right">3.28</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.44</td>
    <td align="right">7.06</td>
    <td align="right">7.06</td>
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
    <td align="right">31.79</td>
    <td align="right">16.61</td>
    <td align="right">6.23</td>
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
    <td align="right">9.89</td>
    <td align="right">8.97</td>
    <td align="right">15.39</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.42</td>
    <td align="right">4.15</td>
    <td align="right">4.01</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.20</td>
    <td align="right">3.70</td>
    <td align="right">3.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">14.30</td>
    <td align="right">13.21</td>
    <td align="right">16.23</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.10</td>
    <td align="right">4.88</td>
    <td align="right">5.40</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.07</td>
    <td align="right">3.51</td>
    <td align="right">3.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">19.43</td>
    <td align="right">16.49</td>
    <td align="right">16.00</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">4.42</td>
    <td align="right">5.18</td>
    <td align="right">5.88</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">5.53</td>
    <td align="right">6.18</td>
    <td align="right">6.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">25.48</td>
    <td align="right">23.61</td>
    <td align="right">16.23</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">6.67</td>
    <td align="right">9.18</td>
    <td align="right">8.76</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">6.73</td>
    <td align="right">7.98</td>
    <td align="right">7.90</td>
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
    <td align="right">10.57</td>
    <td align="right">9.12</td>
    <td align="right">9.11</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.03</td>
    <td align="right">4.73</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.35</td>
    <td align="right">3.60</td>
    <td align="right">3.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.14</td>
    <td align="right">2.23</td>
    <td align="right">2.23</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">4.47</td>
    <td align="right">5.21</td>
    <td align="right">5.28</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.77</td>
    <td align="right">3.73</td>
    <td align="right">3.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">10.88</td>
    <td align="right">11.34</td>
    <td align="right">3.94</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">5.12</td>
    <td align="right">6.34</td>
    <td align="right">6.18</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">5.85</td>
    <td align="right">5.97</td>
    <td align="right">5.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">5.83</td>
    <td align="right">6.15</td>
    <td align="right">4.36</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">3.49</td>
    <td align="right">4.66</td>
    <td align="right">4.53</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">7.14</td>
    <td align="right">8.20</td>
    <td align="right">8.00</td>
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
    <td align="right">20.72</td>
    <td align="right">3.30</td>
    <td align="right">2.30</td>
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
    <td align="right">7.45</td>
    <td align="right">4.74</td>
    <td align="right">13.32</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.35</td>
    <td align="right">1.31</td>
    <td align="right">1.39</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.43</td>
    <td align="right">1.95</td>
    <td align="right">2.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.68</td>
    <td align="right">7.91</td>
    <td align="right">12.39</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.63</td>
    <td align="right">1.50</td>
    <td align="right">1.39</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.42</td>
    <td align="right">3.03</td>
    <td align="right">2.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">14.07</td>
    <td align="right">8.79</td>
    <td align="right">12.21</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.64</td>
    <td align="right">1.78</td>
    <td align="right">1.84</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.46</td>
    <td align="right">3.19</td>
    <td align="right">3.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.58</td>
    <td align="right">11.66</td>
    <td align="right">12.25</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.12</td>
    <td align="right">2.07</td>
    <td align="right">2.00</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.01</td>
    <td align="right">3.82</td>
    <td align="right">4.79</td>
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
    <td align="right">2.01</td>
    <td align="right">1.93</td>
    <td align="right">1.95</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.63</td>
    <td align="right">1.33</td>
    <td align="right">1.49</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.94</td>
    <td align="right">1.95</td>
    <td align="right">1.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.65</td>
    <td align="right">1.52</td>
    <td align="right">1.37</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.75</td>
    <td align="right">1.57</td>
    <td align="right">1.53</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.07</td>
    <td align="right">2.46</td>
    <td align="right">2.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.26</td>
    <td align="right">2.90</td>
    <td align="right">2.16</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.02</td>
    <td align="right">1.76</td>
    <td align="right">1.77</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.27</td>
    <td align="right">2.92</td>
    <td align="right">3.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">3.25</td>
    <td align="right">4.23</td>
    <td align="right">2.21</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.88</td>
    <td align="right">1.60</td>
    <td align="right">1.78</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.26</td>
    <td align="right">4.38</td>
    <td align="right">4.21</td>
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
    <td align="right">26.45</td>
    <td align="right">11.69</td>
    <td align="right">9.01</td>
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
    <td align="right">9.43</td>
    <td align="right">9.90</td>
    <td align="right">18.10</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">2.64</td>
    <td align="right">3.66</td>
    <td align="right">2.92</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.11</td>
    <td align="right">3.45</td>
    <td align="right">3.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">18.15</td>
    <td align="right">24.51</td>
    <td align="right">23.39</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.72</td>
    <td align="right">6.39</td>
    <td align="right">6.81</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.09</td>
    <td align="right">4.11</td>
    <td align="right">6.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">45.77</td>
    <td align="right">37.63</td>
    <td align="right">22.66</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.24</td>
    <td align="right">7.81</td>
    <td align="right">8.25</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">16.37</td>
    <td align="right">12.25</td>
    <td align="right">11.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">68.00</td>
    <td align="right">50.83</td>
    <td align="right">24.71</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">11.17</td>
    <td align="right">10.09</td>
    <td align="right">8.93</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">20.05</td>
    <td align="right">17.92</td>
    <td align="right">18.32</td>
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
    <td align="right">3.13</td>
    <td align="right">4.67</td>
    <td align="right">3.44</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.00</td>
    <td align="right">2.12</td>
    <td align="right">2.86</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.67</td>
    <td align="right">4.70</td>
    <td align="right">4.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.96</td>
    <td align="right">5.19</td>
    <td align="right">7.05</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.78</td>
    <td align="right">5.34</td>
    <td align="right">6.50</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.15</td>
    <td align="right">9.63</td>
    <td align="right">8.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">9.80</td>
    <td align="right">11.25</td>
    <td align="right">6.86</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">8.68</td>
    <td align="right">8.69</td>
    <td align="right">8.76</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">14.74</td>
    <td align="right">12.92</td>
    <td align="right">12.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">11.32</td>
    <td align="right">14.23</td>
    <td align="right">8.65</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.60</td>
    <td align="right">7.84</td>
    <td align="right">7.68</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">18.71</td>
    <td align="right">18.56</td>
    <td align="right">19.60</td>
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
    <td align="right">35.85</td>
    <td align="right">6.29</td>
    <td align="right">3.66</td>
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
    <td align="right">12.16</td>
    <td align="right">12.47</td>
    <td align="right">17.12</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.87</td>
    <td align="right">4.42</td>
    <td align="right">4.22</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.92</td>
    <td align="right">5.70</td>
    <td align="right">5.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.32</td>
    <td align="right">17.72</td>
    <td align="right">17.63</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.94</td>
    <td align="right">4.77</td>
    <td align="right">4.72</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.66</td>
    <td align="right">8.41</td>
    <td align="right">8.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.56</td>
    <td align="right">21.28</td>
    <td align="right">17.09</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.57</td>
    <td align="right">5.42</td>
    <td align="right">5.43</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.45</td>
    <td align="right">10.83</td>
    <td align="right">10.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.93</td>
    <td align="right">27.20</td>
    <td align="right">16.99</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.88</td>
    <td align="right">5.86</td>
    <td align="right">5.87</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">19.79</td>
    <td align="right">14.15</td>
    <td align="right">14.26</td>
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
    <td align="right">8.89</td>
    <td align="right">10.04</td>
    <td align="right">10.01</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.94</td>
    <td align="right">5.30</td>
    <td align="right">5.20</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">12.39</td>
    <td align="right">5.58</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.90</td>
    <td align="right">4.93</td>
    <td align="right">4.13</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.05</td>
    <td align="right">5.97</td>
    <td align="right">6.08</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.28</td>
    <td align="right">8.75</td>
    <td align="right">8.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">8.41</td>
    <td align="right">10.12</td>
    <td align="right">5.50</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.31</td>
    <td align="right">6.66</td>
    <td align="right">6.63</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.20</td>
    <td align="right">10.49</td>
    <td align="right">10.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">9.35</td>
    <td align="right">9.92</td>
    <td align="right">5.62</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.45</td>
    <td align="right">7.42</td>
    <td align="right">7.42</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.95</td>
    <td align="right">12.82</td>
    <td align="right">13.68</td>
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
    <td align="right">45.97</td>
    <td align="right">21.28</td>
    <td align="right">7.43</td>
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
    <td align="right">14.48</td>
    <td align="right">13.25</td>
    <td align="right">17.79</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.01</td>
    <td align="right">4.51</td>
    <td align="right">4.49</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.30</td>
    <td align="right">6.25</td>
    <td align="right">6.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.40</td>
    <td align="right">19.19</td>
    <td align="right">18.59</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.96</td>
    <td align="right">5.78</td>
    <td align="right">5.30</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.10</td>
    <td align="right">10.12</td>
    <td align="right">10.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">34.56</td>
    <td align="right">40.56</td>
    <td align="right">18.74</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">11.12</td>
    <td align="right">6.87</td>
    <td align="right">6.61</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">29.76</td>
    <td align="right">21.31</td>
    <td align="right">21.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">60.77</td>
    <td align="right">64.89</td>
    <td align="right">22.15</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">15.45</td>
    <td align="right">10.90</td>
    <td align="right">10.90</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">29.24</td>
    <td align="right">22.39</td>
    <td align="right">25.18</td>
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
    <td align="right">8.98</td>
    <td align="right">10.15</td>
    <td align="right">10.12</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.80</td>
    <td align="right">5.65</td>
    <td align="right">5.69</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.39</td>
    <td align="right">6.23</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.26</td>
    <td align="right">5.28</td>
    <td align="right">4.43</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.47</td>
    <td align="right">8.46</td>
    <td align="right">8.45</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">25.02</td>
    <td align="right">11.28</td>
    <td align="right">9.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">10.84</td>
    <td align="right">14.27</td>
    <td align="right">7.82</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">12.08</td>
    <td align="right">8.35</td>
    <td align="right">8.88</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">20.81</td>
    <td align="right">13.66</td>
    <td align="right">14.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">15.30</td>
    <td align="right">19.97</td>
    <td align="right">17.23</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">22.81</td>
    <td align="right">14.67</td>
    <td align="right">14.43</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">34.95</td>
    <td align="right">21.43</td>
    <td align="right">28.81</td>
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
    <td align="right">61.02</td>
    <td align="right">29.80</td>
    <td align="right">13.59</td>
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
    <td align="right">27.13</td>
    <td align="right">41.56</td>
    <td align="right">36.41</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.48</td>
    <td align="right">15.96</td>
    <td align="right">15.96</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.12</td>
    <td align="right">20.21</td>
    <td align="right">20.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">36.68</td>
    <td align="right">63.10</td>
    <td align="right">39.35</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.27</td>
    <td align="right">19.39</td>
    <td align="right">19.28</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.31</td>
    <td align="right">26.78</td>
    <td align="right">26.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">47.28</td>
    <td align="right">77.78</td>
    <td align="right">38.13</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.28</td>
    <td align="right">18.54</td>
    <td align="right">18.42</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.97</td>
    <td align="right">33.24</td>
    <td align="right">33.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">56.31</td>
    <td align="right">96.21</td>
    <td align="right">37.42</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.16</td>
    <td align="right">18.80</td>
    <td align="right">18.79</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">35.08</td>
    <td align="right">37.56</td>
    <td align="right">37.51</td>
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
    <td align="right">10.51</td>
    <td align="right">13.54</td>
    <td align="right">13.54</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">15.82</td>
    <td align="right">19.77</td>
    <td align="right">19.73</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.60</td>
    <td align="right">22.15</td>
    <td align="right">22.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.81</td>
    <td align="right">16.46</td>
    <td align="right">15.88</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.05</td>
    <td align="right">18.62</td>
    <td align="right">18.60</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.52</td>
    <td align="right">28.96</td>
    <td align="right">28.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.47</td>
    <td align="right">19.35</td>
    <td align="right">19.36</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.05</td>
    <td align="right">18.60</td>
    <td align="right">18.25</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.99</td>
    <td align="right">45.69</td>
    <td align="right">45.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">23.98</td>
    <td align="right">25.45</td>
    <td align="right">25.43</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.88</td>
    <td align="right">19.96</td>
    <td align="right">19.99</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.38</td>
    <td align="right">55.42</td>
    <td align="right">55.39</td>
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
    <td align="right">71.15</td>
    <td align="right">103.31</td>
    <td align="right">17.61</td>
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
    <td align="right">27.41</td>
    <td align="right">42.86</td>
    <td align="right">39.20</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.76</td>
    <td align="right">16.09</td>
    <td align="right">16.16</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.43</td>
    <td align="right">20.52</td>
    <td align="right">20.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">36.53</td>
    <td align="right">62.57</td>
    <td align="right">41.89</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.25</td>
    <td align="right">19.49</td>
    <td align="right">19.33</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.41</td>
    <td align="right">25.89</td>
    <td align="right">26.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">43.07</td>
    <td align="right">74.57</td>
    <td align="right">40.17</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">17.03</td>
    <td align="right">19.00</td>
    <td align="right">18.92</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.96</td>
    <td align="right">34.61</td>
    <td align="right">33.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">56.17</td>
    <td align="right">95.21</td>
    <td align="right">38.24</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">18.51</td>
    <td align="right">19.83</td>
    <td align="right">19.75</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">36.13</td>
    <td align="right">39.54</td>
    <td align="right">39.09</td>
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
    <td align="right">10.73</td>
    <td align="right">13.79</td>
    <td align="right">13.76</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.14</td>
    <td align="right">19.87</td>
    <td align="right">19.86</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.12</td>
    <td align="right">22.62</td>
    <td align="right">22.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.64</td>
    <td align="right">16.34</td>
    <td align="right">15.74</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.20</td>
    <td align="right">18.84</td>
    <td align="right">18.74</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.22</td>
    <td align="right">29.38</td>
    <td align="right">29.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">14.34</td>
    <td align="right">18.68</td>
    <td align="right">18.70</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">18.18</td>
    <td align="right">18.78</td>
    <td align="right">18.38</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">65.05</td>
    <td align="right">47.15</td>
    <td align="right">47.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">25.99</td>
    <td align="right">28.61</td>
    <td align="right">28.00</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">19.73</td>
    <td align="right">20.96</td>
    <td align="right">21.20</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">80.85</td>
    <td align="right">57.27</td>
    <td align="right">57.20</td>
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
    <td align="right">63.86</td>
    <td align="right">10.64</td>
    <td align="right">7.36</td>
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
    <td align="right">13.93</td>
    <td align="right">23.24</td>
    <td align="right">26.92</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.62</td>
    <td align="right">12.81</td>
    <td align="right">12.51</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.85</td>
    <td align="right">16.19</td>
    <td align="right">16.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.66</td>
    <td align="right">35.21</td>
    <td align="right">29.35</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.27</td>
    <td align="right">14.23</td>
    <td align="right">14.27</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.42</td>
    <td align="right">22.47</td>
    <td align="right">22.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.19</td>
    <td align="right">47.62</td>
    <td align="right">30.17</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.76</td>
    <td align="right">15.54</td>
    <td align="right">15.56</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.30</td>
    <td align="right">32.34</td>
    <td align="right">32.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">32.59</td>
    <td align="right">60.58</td>
    <td align="right">30.47</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.69</td>
    <td align="right">16.51</td>
    <td align="right">16.43</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">30.53</td>
    <td align="right">37.16</td>
    <td align="right">37.20</td>
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
    <td align="right">7.06</td>
    <td align="right">9.42</td>
    <td align="right">9.45</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.82</td>
    <td align="right">14.01</td>
    <td align="right">14.37</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.30</td>
    <td align="right">16.77</td>
    <td align="right">16.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.88</td>
    <td align="right">14.04</td>
    <td align="right">13.99</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.59</td>
    <td align="right">15.54</td>
    <td align="right">15.54</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.90</td>
    <td align="right">22.34</td>
    <td align="right">22.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.31</td>
    <td align="right">17.63</td>
    <td align="right">17.60</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.78</td>
    <td align="right">16.87</td>
    <td align="right">16.90</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.88</td>
    <td align="right">31.28</td>
    <td align="right">31.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">17.26</td>
    <td align="right">21.99</td>
    <td align="right">22.02</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">16.11</td>
    <td align="right">17.99</td>
    <td align="right">18.02</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.23</td>
    <td align="right">36.03</td>
    <td align="right">36.14</td>
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
    <td align="right">92.37</td>
    <td align="right">54.64</td>
    <td align="right">11.71</td>
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
    <td align="right">14.49</td>
    <td align="right">23.36</td>
    <td align="right">28.63</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.84</td>
    <td align="right">12.86</td>
    <td align="right">12.91</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.32</td>
    <td align="right">17.40</td>
    <td align="right">17.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.80</td>
    <td align="right">35.23</td>
    <td align="right">30.90</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">12.66</td>
    <td align="right">15.51</td>
    <td align="right">14.86</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">18.29</td>
    <td align="right">23.40</td>
    <td align="right">23.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">31.19</td>
    <td align="right">68.78</td>
    <td align="right">56.47</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">20.12</td>
    <td align="right">22.32</td>
    <td align="right">19.26</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">32.15</td>
    <td align="right">42.09</td>
    <td align="right">44.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">58.47</td>
    <td align="right">102.67</td>
    <td align="right">43.04</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">30.06</td>
    <td align="right">30.08</td>
    <td align="right">38.76</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">46.77</td>
    <td align="right">58.92</td>
    <td align="right">59.88</td>
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
    <td align="right">7.41</td>
    <td align="right">9.85</td>
    <td align="right">9.81</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">12.29</td>
    <td align="right">14.37</td>
    <td align="right">14.41</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.73</td>
    <td align="right">18.22</td>
    <td align="right">18.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.49</td>
    <td align="right">14.64</td>
    <td align="right">14.57</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">15.67</td>
    <td align="right">17.39</td>
    <td align="right">16.31</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">20.08</td>
    <td align="right">24.12</td>
    <td align="right">24.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">19.62</td>
    <td align="right">22.34</td>
    <td align="right">22.72</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">22.05</td>
    <td align="right">24.91</td>
    <td align="right">27.32</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">32.15</td>
    <td align="right">40.80</td>
    <td align="right">39.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">42.72</td>
    <td align="right">47.52</td>
    <td align="right">46.23</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">28.40</td>
    <td align="right">33.54</td>
    <td align="right">31.98</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">51.68</td>
    <td align="right">55.58</td>
    <td align="right">57.29</td>
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
    <td align="right">44.05</td>
    <td align="right">9.26</td>
    <td align="right">7.16</td>
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
    <td align="right">55.28</td>
    <td align="right">53.61</td>
    <td align="right">37.03</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.21</td>
    <td align="right">17.28</td>
    <td align="right">20.41</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">20.21</td>
    <td align="right">41.61</td>
    <td align="right">40.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">85.83</td>
    <td align="right">78.22</td>
    <td align="right">38.46</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">20.41</td>
    <td align="right">18.83</td>
    <td align="right">20.77</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">24.56</td>
    <td align="right">56.97</td>
    <td align="right">57.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">105.13</td>
    <td align="right">96.77</td>
    <td align="right">37.45</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">21.53</td>
    <td align="right">19.18</td>
    <td align="right">20.43</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">36.39</td>
    <td align="right">76.85</td>
    <td align="right">77.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">135.05</td>
    <td align="right">121.14</td>
    <td align="right">38.03</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">23.74</td>
    <td align="right">20.57</td>
    <td align="right">21.18</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">41.88</td>
    <td align="right">91.30</td>
    <td align="right">91.86</td>
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
    <td align="right">19.01</td>
    <td align="right">29.08</td>
    <td align="right">29.25</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">21.81</td>
    <td align="right">22.50</td>
    <td align="right">25.02</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">23.01</td>
    <td align="right">40.05</td>
    <td align="right">41.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">16.05</td>
    <td align="right">32.50</td>
    <td align="right">24.09</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">23.40</td>
    <td align="right">24.22</td>
    <td align="right">25.23</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">29.17</td>
    <td align="right">56.46</td>
    <td align="right">58.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">26.48</td>
    <td align="right">52.87</td>
    <td align="right">37.10</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">25.89</td>
    <td align="right">26.58</td>
    <td align="right">27.95</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">42.03</td>
    <td align="right">78.16</td>
    <td align="right">78.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0262</td>
    <td align="right">26.01</td>
    <td align="right">51.23</td>
    <td align="right">38.18</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">28.68</td>
    <td align="right">28.85</td>
    <td align="right">29.75</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">48.08</td>
    <td align="right">91.89</td>
    <td align="right">92.37</td>
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
    <td align="right">67.28</td>
    <td align="right">39.94</td>
    <td align="right">14.03</td>
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
    <td align="right">65.31</td>
    <td align="right">57.49</td>
    <td align="right">41.24</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">19.68</td>
    <td align="right">17.91</td>
    <td align="right">22.49</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">22.47</td>
    <td align="right">43.71</td>
    <td align="right">42.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">100.88</td>
    <td align="right">95.69</td>
    <td align="right">43.27</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">23.28</td>
    <td align="right">23.52</td>
    <td align="right">28.93</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">30.15</td>
    <td align="right">64.88</td>
    <td align="right">66.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">160.65</td>
    <td align="right">128.97</td>
    <td align="right">49.39</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">32.84</td>
    <td align="right">27.21</td>
    <td align="right">29.12</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">45.59</td>
    <td align="right">85.96</td>
    <td align="right">87.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">296.78</td>
    <td align="right">247.27</td>
    <td align="right">65.54</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">49.04</td>
    <td align="right">34.38</td>
    <td align="right">38.33</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">62.62</td>
    <td align="right">106.02</td>
    <td align="right">107.76</td>
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
    <td align="right">22.03</td>
    <td align="right">39.00</td>
    <td align="right">33.94</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">24.32</td>
    <td align="right">24.88</td>
    <td align="right">28.64</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">25.40</td>
    <td align="right">44.19</td>
    <td align="right">46.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">19.88</td>
    <td align="right">39.90</td>
    <td align="right">32.26</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">30.90</td>
    <td align="right">28.29</td>
    <td align="right">29.50</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">47.80</td>
    <td align="right">64.55</td>
    <td align="right">74.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">40.08</td>
    <td align="right">76.73</td>
    <td align="right">57.57</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">39.92</td>
    <td align="right">38.83</td>
    <td align="right">41.79</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">59.25</td>
    <td align="right">87.52</td>
    <td align="right">89.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">45.38</td>
    <td align="right">91.98</td>
    <td align="right">82.08</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">47.23</td>
    <td align="right">55.67</td>
    <td align="right">54.54</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">68.64</td>
    <td align="right">111.25</td>
    <td align="right">110.76</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
